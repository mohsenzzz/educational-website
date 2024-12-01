from django.db import models
from ckeditor.fields import RichTextField
from django.core.paginator import Paginator
from django.db.models import Sum,Count
from django.http import HttpResponse
from pyexpat.errors import messages
from ckeditor.fields import RichTextField

from user.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    premium = models.BooleanField(default=False)
    description = models.TextField()
    content = RichTextField()
    image = models.ImageField(upload_to='posts/')

    def __str__(self):
        return self.title

    @classmethod
    def get_posts(cls, page_number):
        posts = cls.objects.all().annotate(comment_count=Count('comments'))
        paginator = Paginator(posts, 1)
        page_obj = paginator.get_page(page_number)
        return page_obj

    @classmethod
    def get_premium_posts(cls, page_number):
        posts = cls.objects.filter(premium=True).annotate(comment_count=Count('comments'))
        paginator = Paginator(posts,1)
        page_obj = paginator.get_page(page_number)
        return page_obj

    @classmethod
    def get_free_posts(cls, page_number):
        posts= Post.objects.filter(premium=False).annotate(comment_count=Count('comments'))
        paginator = Paginator(posts, 1)
        page_obj = paginator.get_page(page_number)
        return page_obj

    @classmethod
    def post_detail(cls,user, post_id):
        try:
            post = cls.objects.filter(id=post_id).prefetch_related('comments').first()


            if post.premium:
                if user.premium is False:
                    message = {'message': 'Sorry you are not premium!\n please buy subscription.', 'premium':False}
                    return message
            comments = post.comments.all().select_related('user').order_by('created_at')
            print(comments[0].user.username)
            context = {'post':post, 'comments':comments}
            return context
        except Exception as e:
            print(e)
            message = {'message': f'post {post_id} not found'}
            return message


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content




class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post= models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

class Category(models.Model):
    title = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.PROTECT)
    posts = models.ManyToManyField('Post', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'
