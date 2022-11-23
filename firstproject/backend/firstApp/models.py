from django.db import models



# Create your models here.
class userDetails(models.Model):
    name = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200)
    district = models.CharField(max_length = 200)
    shop_name = models.CharField(max_length = 200)
    mobilenumber = models.IntegerField(max_length = 10)
    emailId = models.EmailField(max_length = 200,unique=True)
    password = models.CharField(max_length = 20)
# Create your models here.
