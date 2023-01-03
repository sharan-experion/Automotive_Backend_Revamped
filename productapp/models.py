from django.db import models
from firstApp.models import User
class category(models.Model):
    
    categoryname=models.CharField(max_length=200)

# Create your models here.
class products(models.Model):
    productName=models.CharField(max_length=200)
    productPrice=models.DecimalField(max_digits=15, decimal_places=2)
    productQuantity=models.IntegerField()
    categoryId=models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    userId=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
