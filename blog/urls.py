from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_view, name='blog_view'),
    path('<int:pid>', views.blog_single, name='blog_single'),
    path('category/<str:cat_name>', views.blog_view, name='blog_category'),
    path('author/<str:author_username>', views.blog_view, name='blog_author'),
    path('search/', views.blog_search, name='blog_search'),
]   