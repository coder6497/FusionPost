from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.paginator import Paginator
from .forms import RegistrationForm, TextPostForm, EditUserForm, CommentForm
from .models import TextPost, CustomUser, Comment

def index(request):
    post_list = TextPost.objects.filter(private=False)
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "index.html", {"page_obj": page_obj})

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            login(request, form.save())
            return redirect('blogs:post_list')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def create_text_post(request):
    if request.method == 'POST':
        form = TextPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blogs:post_list')
    else:
        form = TextPostForm()
    return render(request, "posts/create_text_post.html", {'form': form})

@login_required
def post_list(request):
    return render(request, 'posts/post_list.html', {"text_posts": TextPost.objects.filter(author=request.user)})


@login_required
def delete_post(request, post_id):
    TextPost.objects.filter(id=post_id).delete()
    return redirect('blogs:post_list')

def text_post_detail(request, text_post_id):
    text_post = TextPost.objects.get(id=text_post_id)
    comments = Comment.objects.filter(post=text_post)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = text_post
            comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'posts/text_post_detail.html', {"text_post": text_post, "comments": comments, "comment_form": comment_form})

@login_required
def edit_post(request, post_id):
    text_post = TextPost.objects.get(id=post_id)
    if request.method == 'POST':
        edit_form = TextPostForm(request.POST, request.FILES, instance=text_post)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('blogs:text_post_detail', text_post_id=text_post.id)
    else:
        edit_form = TextPostForm(instance=text_post)
    return render(request, 'posts/edit_post.html', {'text_post': text_post, 'edit_form': edit_form})

@login_required
def about_user(request): 
    return render(request, 'about_user.html', {"user": CustomUser.objects.get(id=request.user.id)})

@login_required
def edit_user(request):
    if request.method == "POST":
        userform = EditUserForm(request.POST, request.FILES, instance=request.user)
        if userform.is_valid():
            userform.save()
            return redirect('blogs:about_user')
    else:
        userform = EditUserForm(instance=request.user)
    return render(request, 'edit_user.html', {"userform": userform})
