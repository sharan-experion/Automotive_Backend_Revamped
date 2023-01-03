from django.db import models
from django import forms 
from firstApp.models import User
class tbl_Employee(models.Model):    
  #  Id = models.IntegerField()
    Empcode = models.CharField(max_length=10, default='')
    Name = models.CharField(max_length=150,null=True)
    email = models.CharField(max_length=30,null=True)
    phoneNo = models.CharField(max_length=12, default='',null=True)
    address = models.CharField(max_length=500, default='',null=True) 
    exprience = models.CharField(max_length=50, default='',null=True)        
    
    gender = models.CharField(max_length=10, default='',null=True)
    qualification = models.CharField(max_length=50,default='',null=True)
    userId=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.Name
                 
    objects = models.Manager()

# Create your models here.
