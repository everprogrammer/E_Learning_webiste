from django import template
from blog.models import Post, Category

register = template.Library()

@register.simple_tag(name='totalposts')
def total_posts():
    return Post.objects.filter(published_status=1).count()

@register.simple_tag(name='published_posts')
def published_posts():
    posts = Post.objects.filter(published_status=1).order_by('-published_date')[:3]
    return posts


@register.inclusion_tag('blog/blog-sidebar.html')
def recent_posts():
    # Recent posts
    posts = Post.objects.filter(published_status=1).order_by('-published_date')[:3]
    return {'myposts': posts}

# @register.inclusion_tag('blog/blog-category.html')
# def postcategories():
#     posts = Post.objects.filter(published_status=1)
#     categories = Category.objects.all()
#     cat_dict = {}
#     for name in categories:
#         cat_dict[name] = posts.filter(category=name).count()

#     return {'categories': cat_dict}

@register.inclusion_tag('blog/blog-categories.html')
def postcategories():
    posts = Post.objects.filter(published_status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()

    return {'categories': cat_dict}

@register.inclusion_tag('blog/blog-recent-posts.html')
def latest_posts(arg=3):
    posts = Post.objects.filter(published_status=1).order_by('-published_date')[:arg]

    return {'latest_posts': posts}
