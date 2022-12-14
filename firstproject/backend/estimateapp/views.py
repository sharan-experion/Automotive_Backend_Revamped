from django.shortcuts import render
from rest_framework import  status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import  service_Details,CustomerDetails,Estimation_details,Estimate_Services,Estimate_Products
from .serilizer import serviceSerilizer,CustomerSerilizer,EstimateSerilizer,estimateproductSerilizer,estimateServiceSerilizer
from  django.db import connection
from productapp .models import products
from productapp.serilizer import productSerializer

@api_view(['GET'])
def getservices(request):

    service = service_Details.objects.all()
    serializer = serviceSerilizer(service, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def getproduct_for_estimation(request):
    # user=key
    service = products.objects.filter().filter()
    serializer = productSerializer(service, many=True)
    
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['POST'])
def getcustomer(request,key,user):
    vehicleno=key
    userid=user
    print(userid)

    customer = CustomerDetails.objects.filter(userId=userid,vehicleNumber=vehicleno).filter()
    serializer = CustomerSerilizer(customer, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addcustomer(request):
    print(request)
    serializer=CustomerSerilizer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({'message':'Customer Added Successfully'})
    else:
        return Response({'message':'PLEASE ENTER THE VALID DATA'})

@api_view(['POST'])
def addestimate(request):
    
    
    details={'date_of_estimation':request.data['date'],"total_cost":request.data['cost'],"work_status":request.data['status'],
   "vehicleNumber": request.data['vehicleNumber'],"userId":request.data['userId']}
   
    serializer=EstimateSerilizer(data=details)
    serializer.is_valid(raise_exception=True)
    
    serializer.save()
    estimaetid=Estimation_details.objects.filter(vehicleNumber=request.data['vehicleNumber']).last()
    
    id=estimaetid.id
    
    estimatedproduct=request.data['products']
    for item in estimatedproduct:
        item['estimateId']=id
        productserilizer=estimateproductSerilizer(data=item)
        productserilizer.is_valid(raise_exception=True)
        productserilizer.save()
    
    estimateServices=request.data['Services']
    for item in estimateServices:
        item['estimateId']=id
        serviceserilizer=estimateServiceSerilizer(data=item)
        serviceserilizer.is_valid(raise_exception=True)
        serviceserilizer.save()
    return Response({'message':'Estimation Added Successfully'})



   
@api_view(['GET'])
def getservicehistory(request,key,user):
    vehicleno=key
    userid=user
    estimatedetails = Estimation_details.objects.filter(userId=userid,vehicleNumber=vehicleno).filter()
    serializer = EstimateSerilizer(estimatedetails, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def getestimateproduct(request,key):
    estid=key
    estimatedetails = Estimate_Products.objects.filter(estimateId=estid).filter()
    serializer = estimateproductSerilizer(estimatedetails, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getestimateservices(request,key):
    estid=key
    estimateproducts = Estimate_Services.objects.filter(estimateId=estid).filter()
    serializer = estimateServiceSerilizer(estimateproducts, many=True)
    return Response(serializer.data)
    

@api_view(['PUT'])
def update_estimate_product(request):
    estimate_Product=request.data['products']
    for item in estimate_Product:
        proId=item['estimateProductsId']
        pro = products.objects.get(id=proId)
        pro.productQuantity=pro.productQuantity-item['productQuanity']
        pro.save() 
    return Response()

@api_view(['PUT'])
def update_Work_status(request,key):
    status=request.data
    estimation=Estimation_details.objects.get(id=key)
    estimation.work_status=status['status']
    estimation.save()
    return Response()









