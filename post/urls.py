from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.posts_list, name='posts_list'),
    path('premium/', views.posts_premium, name='posts_premium'),
    path('free/', views.posts_free, name='posts_free'),
    path('detail/<int:post_id>', views.post_detail, name='post_detail'),
]