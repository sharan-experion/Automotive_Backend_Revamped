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
   

class Estimation_details(models.Model):
    vehicleNumber=models.ForeignKey(CustomerDetails,on_delete=models.CASCADE,null=True)
    date_of_estimation=models.DateField()
    total_cost=models.DecimalField(max_digits=15, decimal_places=2)
    work_status=models.BooleanField()
    userId=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

class Estimate_Products(models.Model):
    estimateId=models.ForeignKey(Estimation_details,on_delete=models.CASCADE,null=True)
    estimate_product_name=models.CharField(max_length=200)
    estimateProductsId=models.BigIntegerField()
    productQuanity=models.IntegerField()
    productPrice=models.DecimalField(max_digits=15, decimal_places=2 ,null=True)

class Estimate_Services(models.Model):
    estimateId=models.ForeignKey(Estimation_details,on_delete=models.CASCADE,null=True)
    estimate_service_name=models.CharField(max_length=200)
    estimateServiceId=models.BigIntegerField()
    estimatePrice=models.DecimalField(max_digits=15, decimal_places=2 ,null=True)
    

# Create your models here.
