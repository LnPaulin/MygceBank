from django.contrib import admin
from .models import Blog, Category, Comment, Message, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CommentItemInline(admin.TabularInline): 
    model = Comment
    raw_id_fields = ['blog']

class BlogAdmin(admin.ModelAdmin): 
    search_fields = ['title', 'description']
    list_display = ['title', 'date']
    inlines = [CommentItemInline]

class MessageAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email']
    list_display = ['name', 'subject', 'message', 'created_at']


admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)
admin.site.register(Message,MessageAdmin)
admin.site.register(Category,CategoryAdmin)


