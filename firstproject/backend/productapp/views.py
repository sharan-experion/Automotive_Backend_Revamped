from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import category,products
from .serilizer import categorySerializer,productSerializer
from rest_framework.response import Response


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
def displayproducts(request,key):
    userid=key
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

    
    
      




# Create your views here.
