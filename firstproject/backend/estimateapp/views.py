from django.shortcuts import render

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
def getproduct_for_estimation(request,key):
    user=key
    service = products.objects.filter(userId=user).filter()
    serializer = productSerializer(service, many=True)
    
    return Response(serializer.data)


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
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({'message':'Customer Added Successfully'})

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

  
    print("********************************************")
    
    
    return Response({'message':'Estimation Added Successfully'})


# @api_view(['GET'])
# def getservicehistory(request,key):
#     vehicleno=key

#     cursor = connection.cursor()
#     cursor.execute("SELECT estimateapp_estimation_details.date_of_estimation,estimateapp_estimation_details.total_cost,estimateapp_estimation_details.work_status,estimateapp_estimate_products.estimate_product_name,estimateapp_estimate_products.productQuanity,estimateapp_estimate_services.estimate_service_name from estimateapp_estimation_details inner join estimateapp_estimate_products on estimateapp_estimation_details.id=estimateapp_estimate_products.estimateId_id inner join estimateapp_estimate_services on estimateapp_estimation_details.id=estimateapp_estimate_services.estimateId_id where estimateapp_estimation_details.vehicleNumber_id=%s",[vehicleno])

#     result = cursor.fetchall()

#     final_list=[]
#     for item in result:
#         singleitem={}
#         singleitem["date_of_estimation"]=item[0]
#         singleitem["Total_cost"]=item[1]
#         singleitem["Work_status"]=item[2]
#         singleitem["estimate_product_name"]=item[3]
#         singleitem["estimate_qunatity"]=item[4]
#         singleitem["estimate_service_name"]=item[5]
       
#         final_list.append(singleitem)
#     return Response(final_list)
   
@api_view(['GET'])
def getservicehistory(request,key,user):
    vehicleno=key
    userid=user
    estimatedetails = Estimation_details.objects.filter(userId=userid,vehicleNumber=vehicleno).filter()
    serializer = EstimateSerilizer(estimatedetails, many=True)
    return Response(serializer.data)
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
    




# Create your views here.
