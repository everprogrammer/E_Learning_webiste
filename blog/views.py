from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(published_status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-medium-image.html', context)

def blog_single(request, pid):
    posts = Post.objects.filter(published_status=1)
    post = get_object_or_404(posts, pk=pid)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)