from django.contrib import admin
from django.contrib.admin import register
from mptt.admin import MPTTModelAdmin

from .models import Post, Category, Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','premium')
    list_editable = ('premium',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','user','content')

@register(Category)
class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ('title','slug')




admin.site.register(Post,PostAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Comment,CommentAdmin)