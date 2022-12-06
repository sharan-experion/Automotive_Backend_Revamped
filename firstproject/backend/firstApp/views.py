from django.shortcuts import render




# from rest_framework.decorators import authentication_classes,permission_classes
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth.hashers import check_password
# from django.contrib.auth.models import User
from .models import User
from django.contrib.auth import authenticate
from.serializer import userSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view

from rest_framework.response import Response
from django.core import serializers
import jwt,datetime






@api_view(['POST'])

def register(request):
    serializer=userSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)



@api_view(['POST'])
def login(request):
    email=request.data['email']
    password=request.data['password']
    user=User.objects.filter(email=email).first()
    if user is None:
        raise AuthenticationFailed('user not found')
    if not user.check_password(password):
        raise AuthenticationFailed('inncorrect password')
    payload={
        'id':user.id,
        'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=10),
        'iat':datetime.datetime.utcnow()
    }
    token=jwt.encode(payload,'secret',algorithm='HS256')
    response=Response()
    response.set_cookie(key='jwt',value=token,httponly=True)
    response.data={
        'jwt':token,'username':user.name,"userID":user.id

    }
    print(response)
    
    return response



@api_view(['GET'])
def userview(request):
    token=request.COOKIES.get('jwt')
    
    if not token:
        raise AuthenticationFailed('Unauthenticated!')
    try:
        payload=jwt.decode(token,'secret',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')
    user=User.objects.filter(id=payload['id']).filter()
    serializers=userSerializer(user,many=True)

    return Response(serializers.data)

@api_view(['POST'])
def logout(request):
    response=Response()
    response.delete_cookie('jwt')
    response.data={
        'message':'sucess'
    }
    return response





# @api_view(['POST'])
# def postuserdetails(request):

#     data = request.data.copy()
#     data_password=request.POST.get('password')
#     password=make_password(data_password)
#     data['password']=password

#     serializer = userSerializer(data=data)

#     # print(serializer)

#     if(serializer.is_valid()):
#         serializer.save()
#         return Response({'status':1,'message':'Successfully Saved','data':serializer.data})
#     else:
#         return Response({'status':0,'message':'OOPS Some error occured','data':serializer.errors})



# @api_view(['POST'])
# def logindetails(request):
   
        
    
#     return Response({'satus':'Done'})








  



# Create your views here
