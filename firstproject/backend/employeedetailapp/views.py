from django.shortcuts import render

from .models import tbl_Employee
import datetime as dt
import pandas as pd
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serilizer import employeeSerializer

from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime

@api_view(['POST'])
def Import_csv(request):
        if request.method == 'POST' and request.FILES['employeedetails']:
            empexceldata = pd.read_excel(request.FILES['employeedetails'] )
            print(empexceldata)
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():
                obj = tbl_Employee.objects.create(Empcode=dbframe.Empcode,Name=dbframe.Name,
                                                 email=dbframe.email, phoneNo=dbframe.phoneNo, address=dbframe.address, 
                                                exprience=dbframe.exprience, gender=dbframe.gender,
                                                qualification=dbframe.qualification,userId_id=dbframe.userId)
                obj.save()
        return Response({'message':'File Added Successfully'})


@api_view(['GET'])
def displayemployee(request,key):
    userid=key
    data_list =tbl_Employee.objects.filter(userId=userid).filter()
    print(data_list)
    serializer = employeeSerializer(data_list, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def singleEmployee(request):
    serializer=employeeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({'message':'Customer Added Successfully'})


 
# Create your views here.
