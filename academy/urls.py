"""
URL configuration for academy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from azbankgateways.urls import az_bank_gateways_urls
from subscription import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('user/',include('user.urls')),
    path('post/',include('post.urls')),
    path("bankgateways/", az_bank_gateways_urls()),
    path('go_to_gateway/<int:pk>',views.go_to_gateway_view,name='go_to_gateway'),
    path('callback_gateway/',views.callback_gateway_view,name='callback_gateway'),
    path('subscription/',include('subscription.urls')),

]
