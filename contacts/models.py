from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=250, default="", null=False)
    address1 = models.TextField(max_length=1024, null=False)
    address2 = models.TextField(max_length=1024, null=False)
    zipcode = models.CharField(max_length=5, null=False)
    city = models.CharField(max_length=250, null=False)
    user = models.ManyToManyField(User)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
