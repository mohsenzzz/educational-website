from django.shortcuts import render
from rest_framework.decorators import api_view

from post.models import Post


# Create your views here.

@api_view(['GET'])
def posts_list(request, page=1):

    page_obj = Post.get_posts(request.GET.get('page'))
    return render(request, 'post/posts.html', {'page_obj': page_obj})

@api_view(['GET'])
def posts_premium(request):
    page_obj = Post.get_premium_posts(request.GET.get('page'))
    return render(request, 'post/posts.html', {'page_obj': page_obj})

@api_view(['GET'])
def posts_free(request):
    page_obj = Post.get_free_posts(request.GET.get('page'))
    return render(request, 'post/posts.html', {'page_obj': page_obj})

@api_view(['GET'])
def post_detail(request, post_id):
    context = Post.post_detail(request.user,post_id)

    return render(request, 'post/post_detail.html', context)
