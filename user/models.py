from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    phone_number = PhoneNumberField()
    premium = models.BooleanField(default=False)
    expire_time = models.DateTimeField(null=True)
    subscription = models.ForeignKey('Subscription',on_delete = models.CASCADE, related_name='users', null=True)



class Subscription(models.Model):
    title = models.CharField(max_length=100)
    price =models.BigIntegerField()

