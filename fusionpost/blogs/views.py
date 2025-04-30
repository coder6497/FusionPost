from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegistrationForm, TextPostForm
from .models import TextPost

def index(request):
    return render(request, "index.html")

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
        form = TextPostForm(request.POST)
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
    return render(request, 'posts/post_list.html', {"text_posts": TextPost.objects.filter(author=request.user).all()})


@login_required
def delete_post(request, post_id):
    TextPost.objects.filter(id=post_id).delete()
    return redirect('blogs:post_list')


@login_required
def text_post_detail(request, text_post_id):
    return render(request, 'posts/text_post_detail.html', {"text_post": TextPost.objects.get(id=text_post_id)})