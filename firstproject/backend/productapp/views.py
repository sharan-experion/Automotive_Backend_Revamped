from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import category,products
from .serilizer import categorySerializer,productSerializer
from rest_framework.response import Response
from .utils import html_to_pdf
from django.template.loader import render_to_string
from django.http import HttpResponse
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import viewsets
import jwt,datetime
from rest_framework import status
import pandas as pd
@api_view(['GET'])
def getcategory(request):

    data_list = category.objects.all()
    serializer = categorySerializer(data_list, many=True)
    
    return Response(serializer.data,status=status.HTTP_201_CREATED)



@api_view(['POST'])
def addproducts(request):
    token= request.headers['Authorization']
    if not token:
        raise AuthenticationFailed('Unauthenticated!')
    try:
        payload=jwt.decode(token,'secret',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')
    
    serializer=productSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response({'message':'Product Added Successfully'})


@api_view(['GET'])
def displayproducts(request):
    token= request.headers['Authorization']
    if not token:
        raise AuthenticationFailed('Unauthenticated!')
    try:
        payload=jwt.decode(token,'secret',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')
    # userid=payload['id']
    data_list =products.objects.filter().filter()
    print(data_list)
    serializer = productSerializer(data_list, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def sortproduct(request):
    categoryid=request.data['id']
    details=products.objects.filter(categoryId=categoryid).filter()
    detailserilizer=productSerializer(details,many=True)
    return Response(detailserilizer.data)


@api_view(['PUT'])
def updateproduct(request,pk):
    
    data =request.data
    product = products.objects.get(id=pk)
    product.productName=data['name']
    product.productPrice=data['price']
    product.productQuantity=data['quantity']
    
    product.save()
    serilizer=productSerializer(product,many=False)
    return Response(serilizer.data)


class printproductdetails(viewsets.ModelViewSet):
    def list(self,request,*args,**kwargs):
        data=products.objects.filter().filter()
        open('templates/temp.html',"w").write(render_to_string('productdetaills.html',{'data':data}))
        pdf=html_to_pdf('temp.html')
        return HttpResponse(pdf,content_type="application/pdf")
# @api_view(['GET'])
# def printproductdetails(request):
#     # userid=key
#     data=products.objects.filter().filter()
#     open('templates/temp.html',"w").write(render_to_string('productdetaills.html',{'data':data}))
#     pdf=html_to_pdf('temp.html')
#     return HttpResponse(pdf,content_type="application/pdf")

@api_view(['POST'])
def productexcel(request):
        if request.method == 'POST' and request.FILES['productdetails']:
            empexceldata = pd.read_excel(request.FILES['productdetails'] )
            print(empexceldata)
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():
                obj = products.objects.create(productName=dbframe.productName,productPrice=dbframe.productPrice,
                                                 productQuantity=dbframe.productQuntity,categoryId_id=dbframe.categoryId,userId_id=dbframe.userId)
                obj.save()
        return Response({'message':'File Added Successfully'})
    
    
      




# Create your views here.
