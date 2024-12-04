from django.db import models
from django.core.paginator import Paginator
from django.db.models import Sum,Count
from django.shortcuts import get_object_or_404
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey

from user.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    premium = models.BooleanField(default=False)
    description = models.TextField()
    content = RichTextField()
    categories = models.ManyToManyField('Category',)
    image = models.ImageField(upload_to='posts/',null=True,blank=True)

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
            print(post)

            if post.premium:
                if user.premium is False:
                    message = {'message': 'Sorry you are not premium!\n please buy subscription.', 'premium':False}
                    return message
            comments = post.comments.all().select_related('user').order_by('created_at')

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

    @classmethod
    def create_comment(cls, user, post_id , content):

        post = get_object_or_404(Post,pk=post_id)
        if post:
            Comment.objects.create(user=user, post=post, content=content)
            return True
        else:
            return False



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post= models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

class Category(MPTTModel):
    title = models.CharField(max_length=200)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200,default="",allow_unicode=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        print('1111111111111111111111111111111111111111')

        print('222222222222222222222222')
        self.slug = slugify(self.title,allow_unicode=True)
        if self.parent:
            print('33333333333333333333333')
            self.slug = f'{self.parent.slug}-{self.slug}'
        super(Category,self).save(*args, **kwargs)

    @classmethod
    def get_categories(cls):
        categories = Category.objects.all()
        return categories

    @classmethod
    def get_all_posts_by_category(cls,category_slug,page_number):
        # category = get_object_or_404(Category, slug=category_slug)
        # posts = Post.objects.filter(categories=category)
        posts = Post.objects.prefetch_related('categories').filter(categories__slug=category_slug)
        paginator = Paginator(posts, 1)
        page_obj = paginator.get_page(page_number)
        return page_obj

    @classmethod
    def get_premium_posts_by_category(cls, category_slug, page_number):
        # category = get_object_or_404(Category, slug=category_slug)
        # posts = Post.objects.filter(categories=category)
        posts = Post.objects.prefetch_related('categories').filter(categories__slug=category_slug,premium=True)
        paginator = Paginator(posts, 1)
        page_obj = paginator.get_page(page_number)
        return page_obj

    @classmethod
    def get_free_posts_by_category(cls, category_slug, page_number):
        # category = get_object_or_404(Category, slug=category_slug)
        # posts = Post.objects.filter(categories=category)
        posts = Post.objects.prefetch_related('categories').filter(categories__slug=category_slug,premium=False)
        paginator = Paginator(posts, 1)
        page_obj = paginator.get_page(page_number)
        return page_obj


