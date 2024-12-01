from django.contrib import admin
from .models import Post, Category, Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','premium')
    list_editable = ('premium',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','user','content')

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
# admin.site.register(Comment,CommentAdmin)