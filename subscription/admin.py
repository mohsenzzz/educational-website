from django.contrib import admin

from subscription.models import Subscription


# Register your models here.

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('title','validity')
