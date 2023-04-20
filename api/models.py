from django.db import models

class Post (models.Model):
    title= models.CharField(max_length=100, null=False,blank=False)
    body= models.TextField()
    user= models.IntegerField(null=False)
    date= models.DateTimeField(auto_now_add=True)
    