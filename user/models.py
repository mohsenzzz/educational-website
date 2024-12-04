from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    phone_number = PhoneNumberField(unique=True,default='09333333333')
    premium = models.BooleanField(default=False)
    expire_time = models.DateTimeField(null=True, blank=True)
    subscription = models.ForeignKey('Subscription',on_delete = models.CASCADE, related_name='users', null=True,blank=True)
    is_active = models.BooleanField(default=False)



class Subscription(models.Model):
    title = models.CharField(max_length=100)
    price =models.BigIntegerField()

