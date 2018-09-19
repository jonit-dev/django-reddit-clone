from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    description = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User)
    votes_total = models.IntegerField(default=0)



def __str__(self):  # title on dashboard
    return self.title
