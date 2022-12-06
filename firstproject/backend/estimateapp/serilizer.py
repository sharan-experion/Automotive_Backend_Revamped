from rest_framework import serializers
from .models import service_Details,CustomerDetails,Estimation_details,Estimate_Products,Estimate_Services
class serviceSerilizer(serializers.ModelSerializer):
    class Meta:
        model=service_Details
        fields=('__all__')

class CustomerSerilizer(serializers.ModelSerializer):
    class Meta:
        model=CustomerDetails
        fields=('__all__')
class EstimateSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Estimation_details
        fields=('__all__')
class estimateproductSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Estimate_Products
        fields=('__all__')

class estimateServiceSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Estimate_Services
        fields=('__all__')