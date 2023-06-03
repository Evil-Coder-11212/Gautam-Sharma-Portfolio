from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blogs(models.Model):
    author = models.CharField( max_length=75, blank=True, null=True)
    image = models.CharField( max_length=75, blank=True, null=True)
    title  = models.CharField( max_length=100, blank=True, null=True)
    paragraph_1 = models.TextField( max_length=500, blank=True, null=True)
    paragraph_2 = models.TextField( max_length=500, blank=True, null=True)
    paragraph_3 = models.TextField( max_length=500, blank=True, null=True)
    paragraph_4 = models.TextField( max_length=500, blank=True, null=True)
    email = models.EmailField( max_length=254, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title+" | " + self.author 