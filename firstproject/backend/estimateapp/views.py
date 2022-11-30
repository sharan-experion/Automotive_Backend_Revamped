from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import  service_Details,CustomerDetails
from .serilizer import serviceSerilizer,CustomerSerilizer


@api_view(['GET'])
def getservices(request):

    service = service_Details.objects.all()
    serializer = serviceSerilizer(service, many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def getcustomer(request,key):
    vehicleno=key

    customer = CustomerDetails.objects.filter(vehicleNumber=vehicleno).filter()
    serializer = CustomerSerilizer(customer, many=True)
    return Response(serializer.data)


# Create your views here.
