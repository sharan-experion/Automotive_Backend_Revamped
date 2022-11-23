from django.shortcuts import render

from django.http import JsonResponse
from .models import userDetails




from .serializer import userSerializer

from rest_framework.decorators import api_view

from rest_framework.response import Response
from django.core import serializers

# @api_view(['GET'])
# def getRoutes(request):
#     routes=[
#         # '/api/products',
#         # '/api/products/creates',
#         # '/api/products/upload',
#         # '/api/products/<id>/',
#     ]
#     return Response(routes)




# @api_view(['GET'])
# def getmealitem(request):
#     data_list = fooditems.objects.all()
#     serializer = foodSerializer(data_list, many=True)
    
#     return Response(serializer.data)

@api_view(['POST'])

def postuserdetails(request):

    data = request.data.copy()

    serializer = userSerializer(data=data)

    if(serializer.is_valid()):

        serializer.save()

        return Response({'status':1,'message':'Successfully Saved','data':serializer.data})

    else:

        return Response({'status':0,'message':'OOPS Some error occured','data':serializer.errors})
    
    



# Create your views here
