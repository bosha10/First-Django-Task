from django.db import models
from django.contrib.auth.models import User
# from django import forms

class Post(models.Model):
    user = models.ForeignKey(User)
    posts = models.CharField(max_length = 500)

    # def __unicode__(self):
    #     return self.posts
