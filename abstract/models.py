from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('title','user_id')
        abstract= True


class Abs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    amount = models.FloatField()
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)

    class Meta:
        abstract = True

