from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required

from post.forms import CommentForm
from post.models import Post, Comment, Category


# Create your views here.
@login_required
@api_view(['GET'])
def posts_list(request):

    page_obj = Post.get_posts(request.GET.get('page'))

    categories = Category.get_categories()
    return render(request, 'post/posts.html', {'page_obj': page_obj, 'categories':categories,'filters':'all'})

@login_required
@api_view(['GET'])
def post_detail(request, post_id):
    context = Post.post_detail(request.user,post_id)
    # comment_form = CommentForm()
    # context['comment_form'] = comment_form
    return render(request, 'post/post_detail.html', context)

@login_required
@api_view(['POST'])
def add_comment(request, post_id):
    result = Comment.create_comment(request.user,post_id,request.POST['comment'])
    if result:
        return redirect('post_detail', post_id)
    else:
        return render(request, 'post/post_detail.html', {'message': f'selected post {post_id} not found or you don\'t login!'})

@login_required
@api_view(['GET'])
def all_posts_category(request, slug):

    page_obj = Category.get_all_posts_by_category(slug,request.GET.get('page'))
    categories = Category.get_categories()
    return render(request, 'post/posts.html', {'page_obj': page_obj, 'categories':categories})


@login_required
@api_view(['GET'])
def premium_posts_category(request, slug):
    page_obj = Category.get_all_posts_by_category(slug,request.GET.get('page'))
    categories = Category.get_categories()
    return render(request, 'post/posts.html', {'page_obj': page_obj, 'categories':categories})
