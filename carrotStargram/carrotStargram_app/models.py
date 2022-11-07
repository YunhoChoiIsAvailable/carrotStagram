from django.db import models

# Create your models here.


class Account(models.Model):
    name = models.charField(max_length=50)
    description = models.charField(max_length=100)



class FriendTable(models.Model):
    people1 = models.ManyToManyField(Account)





class Post(models.Model):
    name = models.CharField(max_length=50)
    description = models.charField(max_length=100)
    link = models.URLField(max_length=200)
    uploader = models.ForeignKey(Account, on_delete=models.CASCADE)
