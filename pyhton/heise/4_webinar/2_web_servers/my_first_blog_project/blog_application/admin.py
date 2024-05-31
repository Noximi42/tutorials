from django.contrib import admin

from .models import BlogPost, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class BlogPostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(BlogPost, BlogPostAdmin)
