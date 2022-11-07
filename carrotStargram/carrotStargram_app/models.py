from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.charField(max_length=50)
    description = models.charField(max_length=100)
    account_img = models.ImageField(upload_to='profiles_imgs')

class FriendTable(models.Model):
    people1 = models.ForeignKey(Account)
    people2 = models.ForeignKey(Account)

class Post(models.Model):
    name = models.CharField(max_length=50)
    description = models.charField(max_length=100)
    link = models.URLField(max_length=200)
    uploader = models.ForeignKey(Account, on_delete=models.CASCADE)
    like = models.ManyToManyField(Account)
    post_img = models.ImageField(upload_to='post_imgs')

