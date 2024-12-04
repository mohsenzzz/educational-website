from django.db import models

from user.models import User


# Create your models here.


class Subscription(models.Model):
    title = models.CharField(max_length=100)
    validity= models.IntegerField()
    description = models.TextField(default='')
    price = models.IntegerField()
    users = models.ForeignKey(User, on_delete=models.PROTECT, null=True,related_name='subscriptions', blank=True)

    def __str__(self):
        return self.title