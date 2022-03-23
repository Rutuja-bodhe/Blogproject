from audioop import add
from distutils.command.upload import upload
from email.mime import image
from statistics import mode
from turtle import onclick, title
from django.db import models
from django.contrib.auth.models import User

class Add_Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank = True, null = True)
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    like = models.ManyToManyField(User, onclick)
    date = models.DateField(auto_now_add=True)

    def __self__(self):
        return self.title[:50]
