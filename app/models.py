from django.db import models
from django.contrib.auth.models import User


class Trending(models.Model):
    theme = models.CharField(max_length=50)
    data =  models.IntegerField(default=0)
class Previous_date(models.Model):
    year_month = models.IntegerField()
    time = models.IntegerField()
    comments = models.TextField(max_length=100)
    like = models.ManyToManyField(User, related_name='liked_posts', blank=True)







