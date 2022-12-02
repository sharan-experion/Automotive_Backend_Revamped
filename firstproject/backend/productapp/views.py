from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import category,products
from .serilizer import categorySerializer,productSerializer
from rest_framework.response import Response
from .utils import html_to_pdf
from django.template.loader import render_to_string
from django.http import HttpResponse
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime
@api_view(['GET'])
def getcategory(request):

    data_list = category.objects.all()
    serializer = categorySerializer(data_list, many=True)
    
    return Response(serializer.data)



@api_view(['POST'])
def addproducts(request):
    print(request)
    serializer=productSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({'message':'Product Added Successfully'})


@api_view(['GET'])
def displayproducts(request):
    a = request.headers['Authorization']
    token= a.split()[1].replace('"', '')
    if not token:
        raise AuthenticationFailed('Unauthenticated!')
    try:
        payload=jwt.decode(token,'secret',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')
    userid=payload['id']
    data_list =products.objects.filter(userId=userid).filter()
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

@api_view(['GET'])
def printproductdetails(request,key):
    userid=key
    data=products.objects.filter(userId=userid).filter()
    open('templates/temp.html',"w").write(render_to_string('productdetaills.html',{'data':data}))
    pdf=html_to_pdf('temp.html')
    return HttpResponse(pdf,content_type="application/pdf")

    
    
      




# Create your views here.
