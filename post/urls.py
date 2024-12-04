from django.urls import path, re_path
from . import views

urlpatterns = [

    path('all/', views.posts_list, name='posts_list'),

    # path('premium/', views.posts_premium, name='posts_premium'),
    # path('free/', views.posts_free, name='posts_free'),
    path('all/(?P<slug>[-\w]+)/', views.all_posts_category, name='all_posts_category'),

    # re_path(r'premium/(?P<slug>[-\w]+)/', views.premium_posts_category, name='premium_posts_category'),
    # path('all/', views.posts_list, name='posts_list'),
    # path('premium/<slug:category_slug>', views.posts_category, name='post_detail'),
    # path('free/<slug:category_slug>', views.posts_category, name='post_detail'),
    path('detail/<int:post_id>', views.post_detail, name='post_detail'),

    path('comment/<int:post_id>', views.add_comment, name='add_comment'),
]