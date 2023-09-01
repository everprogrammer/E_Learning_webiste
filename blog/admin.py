from django.contrib import admin
from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'published_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_views', 'published_status', 'published_date')
    list_filter = ('published_status', 'published_date', 'author')
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'is_approved', 'created_date')
    list_filter = ('post', 'is_approved',)
    search_fields = ['name', 'post']



admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
