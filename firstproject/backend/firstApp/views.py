from django.shortcuts import render

from django.http import JsonResponse
from .models import userDetails

from rest_framework.decorators import authentication_classes,permission_classes


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

    # print(serializer)

    if(serializer.is_valid()):
        serializer.save()
        return Response({'status':1,'message':'Successfully Saved','data':serializer.data})
    else:
        return Response({'status':0,'message':'OOPS Some error occured','data':serializer.errors})
    



# for login authentication...

# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def example_view(request, format=None):
#     content = {
#         'user': str(request.user),  # `django.contrib.auth.User` instance.
#         'auth': str(request.auth),  # None
#     }
#     return Response(content)


# for password encription

# from django.contrib.auth.hashers import make_password
# crew_password = 'take the input if you are using form'
# form = FormName(commit=False)
# form.crew_password=make_password(crew_password)
# form.save()

# Create your views here
