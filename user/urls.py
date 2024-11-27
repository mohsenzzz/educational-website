from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('verify/',views.verify_user, name='verify_user'),
    path('login/',views.login, name='login'),
    # path('verify_profile/',views.get_verify_profile, name='verify_profile'),
    path('profile/',views.get_profile, name='profile'),
    path('edit-profile/<int:pk>',views.edit_profile, name='edit_profile'),
]