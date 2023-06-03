from django.db import models

# Create your models here.
class ContactData(models.Model):
    full_name = models.CharField( max_length=75, blank=True, null=True)
    message = models.TextField( max_length=918, blank=True, null=True)
    subject = models.CharField( max_length=75, blank=True, null=True)
    email = models.EmailField( max_length=254, blank=True, null=True)

    def __str__(self):
        return self.full_name

