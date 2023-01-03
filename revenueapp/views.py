from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from estimateapp.models import Estimation_details
from estimateapp.serilizer import EstimateSerilizer



@api_view(['GET'])
def getrevenuereport(request,key):
    user=key
    estimatedetails = Estimation_details.objects.filter(userId=user).filter()
    
    chartdata={}
    for index in estimatedetails:
        key=str(index.date_of_estimation)
        if key in chartdata.keys():
            chartdata[key]+=int(index.total_cost)
        else:
            chartdata[key]=int(index.total_cost)
    
        
   
    return Response(chartdata)

# Create your views here.
