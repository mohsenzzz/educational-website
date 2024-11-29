from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('verify/',views.verify_user, name='verify_user'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),

    path('profile/',views.get_profile, name='profile'),
    path('edit-profile/<int:pk>',views.edit_profile, name='edit_profile'),
    path('reset-passwoord/<int:pk>',views.reset_password, name='reset_password'),
]