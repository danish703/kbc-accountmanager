from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('title','user_id')
        abstract= True


class Abs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    amount = models.FloatField()
    date = models.DateField(auto_now=True)
    slug = AutoSlugField(populate_from='title')

    class Meta:
        abstract = True

