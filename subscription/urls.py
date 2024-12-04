from django.urls import path
from . import views

urlpatterns = [
    path('',views.SubscriptionView.as_view(),name='subscription'),

]