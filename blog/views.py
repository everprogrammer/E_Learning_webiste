from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def blog_view(request, **kwargs):
    posts = Post.objects.filter(published_status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])

    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts': posts}
    return render(request, 'blog/blog-medium-image.html', context)

def blog_single(request, pid):
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your message sent successfully!')
        else:
            messages.add_message(request, messages.ERROR, 'Your comment was not sent!')
    posts = Post.objects.filter(published_status=1)
    post = get_object_or_404(posts, pk=pid)
    post.increase_views()
    next_post = Post.objects.filter(id__gt=post.id).order_by('id').first()
    previous_post = Post.objects.filter(id__lt=post.id).order_by('-id').first()
    comments = Comment.objects.filter(post=post.id, is_approved=True)
    form = CommentForm()
    context = {'post': post, 'comments': comments, 'form': form,
               'next_post': next_post, 'previous_post': previous_post}
    return render(request, 'blog/blog-single.html', context)

def blog_search(request):
    posts = Post.objects.filter(published_status=1)
    if request.method == 'GET':
        posts = posts.filter(content__contains=request.GET.get('s'))

    context = {'posts': posts}
    return render(request, 'blog/blog-medium-image.html', context)  