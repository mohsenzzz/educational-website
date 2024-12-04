from django.urls import path
from . import views

urlpatterns = [
    path('',views.SubscriptionView.as_view(),name='subscription'),
    path('go_to_gateway/<int:pk>',views.go_to_gateway_view,name='go_to_gateway'),
    path('callback_gateway/<int:days>',views.callback_gateway_view,name='callback_gateway'),
]