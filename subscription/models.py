from django.db import models




# Create your models here.


class Subscription(models.Model):
    title = models.CharField(max_length=100)
    validity= models.IntegerField()
    description = models.TextField(default='')
    price = models.IntegerField()


    def __str__(self):
        return self.title