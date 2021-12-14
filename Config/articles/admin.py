from django.contrib import admin
from .models import Article, Comment

# Register your models here.
class CommentInline(admin.StackedInline): # new
    model = Comment

class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [
        CommentInline,
    ]

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class CommentInline(admin.TabularInline): # new
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)