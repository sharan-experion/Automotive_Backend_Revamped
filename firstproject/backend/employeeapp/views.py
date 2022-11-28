from django.shortcuts import render

from .models import tbl_Employee
import datetime as dt
import pandas as pd
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def Import_csv(request):
    # print('s')               
    # try:
        if request.method == 'POST' and request.FILES['employeedetails']:
          
            myfile = request.FILES['employeedetails']        
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print(excel_file) 
            empexceldata = pd.read_excel('employeedetails.xlsx')
            # empexceldata = pd.read_csv('employeedetails.xlsx',encoding='utf-8')
            print(type(empexceldata))
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():
                 
                # fromdate_time_obj = dt.datetime.strptime(dbframe.DOB, '%d-%m-%Y')
                obj = tbl_Employee.objects.create(Empcode=dbframe.Empcode,Name=dbframe.Name,
                                                 email=dbframe.email, phoneNo=dbframe.phoneNo, address=dbframe.address, 
                                                exprience=dbframe.exprience, gender=dbframe.gender,
                                                qualification=dbframe.qualification,userId=dbframe.userId)
                print(type(obj))
                obj.save()
        return Response()
 
    #         return render(request, 'importexcel.html', {
    #             'uploaded_file_url': uploaded_file_url
    #         })    
    # except Exception as identifier:            
    #     print(identifier)
     
    # return render(request, 'importexcel.html',{})

# Create your views here.
