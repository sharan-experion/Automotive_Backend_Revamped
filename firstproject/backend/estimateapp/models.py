from django.db import models
from firstApp.models import User
from phonenumber_field.modelfields import PhoneNumberField

class service_Details(models.Model):
    services=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=15, decimal_places=2)
    
class CustomerDetails(models.Model):
    name=models.CharField(max_length=200)
    mobileNumber=PhoneNumberField(null=False, blank=False, unique=True)
    vehicleNumber=models.CharField(max_length=200,primary_key=True)
    vehicleType=models.CharField(max_length=200)
    engineNumber=models.CharField(max_length=200)
    chaseNumber=models.CharField(max_length=200)
    userId=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   

# Create your models here.
