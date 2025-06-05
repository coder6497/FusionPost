from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.paginator import Paginator
from django.contrib.postgres.search import SearchVector
from .forms import RegistrationForm, TextPostForm, EditUserForm, CommentForm, SearchForm
from .models import TextPost, CustomUser, Comment, PhotoForGallery
from .parameters import get_params_for_createobject, get_params_for_getobject
from django.http import Http404
from django.db.models import Q
import os

def index(request):
    if request.user.is_authenticated:
        post_list = TextPost.objects.filter(Q(private=False) | Q(author=request.user))
    else:
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
def create_post(request, post_type):
    post_params = get_params_for_createobject(request.POST, request.FILES)
    if request.method == 'POST':
        form = post_params["forms_by_tags"][post_type][0]
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            match post_type:
                case "text_post":
                    return redirect('blogs:post_list')
                case "photo_gallery":
                    return redirect("blogs:create_post", post_type=post_type)
    else:
        form = post_params["forms_by_tags"][post_type][1]

    template = post_params["templates_by_post_type"][post_type]

    template_params = {'form': form,
                       "header": post_params["headers"][post_type],
                       "photos": PhotoForGallery.objects.filter(author=request.user)}
    return render(request, template, template_params)

@login_required
def post_list(request):
    return render(request, 'posts/post_list.html', {"posts": TextPost.objects.filter(author=request.user)})

@login_required
def delete_post(request, post_id, post_type):
    post_params = get_params_for_getobject()
    post_params[post_type].objects.filter(id=post_id).delete()
    match post_type:
        case "text_post":
            return redirect('blogs:post_list')
        case "photo_gallery":
            return redirect('blogs:create_post', post_type=post_type)

def post_detail(request, post_id, post_type):
    post_params = get_params_for_getobject()
    post = post_params[post_type].objects.get(id=post_id)

    is_unauthorized = post.author != request.user
    is_private_text = post_type == 'text_post' and post.private
    is_photo_gallery = post_type == 'photo_gallery'
    if is_unauthorized and (is_private_text or is_photo_gallery):
            raise Http404("Запись не найдена или недоступна")
    
    comments, comment_form = None, None
    if post_type == "text_post":
        comments = Comment.objects.filter(post=post)
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
        else:
            comment_form = CommentForm()

    params = {"post": post, "comments": comments, "comment_form": comment_form, "post_type": post_type}
    return render(request, 'posts/post_detail.html', params)

@login_required
def edit_post(request, post_id):
    text_post = TextPost.objects.get(id=post_id)
    if request.method == 'POST':
        edit_form = TextPostForm(request.POST, request.FILES, instance=text_post)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('blogs:post_detail', post_id=text_post.id, post_type="text_post")
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


def search_posts(request):
    query = None
    form = SearchForm()
    result = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            search_vector = SearchVector('title', 'body', config='russian')
            query = form.cleaned_data['query']
            if request.user.is_authenticated:
                result = TextPost.objects.annotate(search=search_vector
                                                   ).filter(Q(search=query) & (Q(author=request.user) | Q(private=False)))
            else:
                result = TextPost.objects.annotate(search=search_vector).filter(Q(search=query) & Q(private=False))
    return render(request, 'posts/post_search.html', {'result': result, 'query': query, 'form': form})
