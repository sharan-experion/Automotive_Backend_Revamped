from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username=None
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200,unique=True)
    password = models.CharField(max_length = 200)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []












# # Create your models here.
# class userDetails(models.Model):
#     name = models.CharField(max_length = 200)
#     state = models.CharField(max_length = 200)
#     district = models.CharField(max_length = 200)
#     shop_name = models.CharField(max_length = 200)
#     mobilenumber = models.IntegerField(max_length = 10)
#     emailId = models.EmailField(max_length = 200,unique=True)
#     password = models.CharField(max_length = 200)

#     def _str_(self):
#      return self.name
# Create your models here.
