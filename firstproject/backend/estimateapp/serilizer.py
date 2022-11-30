from rest_framework import serializers
from .models import service_Details,CustomerDetails
class serviceSerilizer(serializers.ModelSerializer):
    class Meta:
        model=service_Details
        fields=('__all__')

class CustomerSerilizer(serializers.ModelSerializer):
    class Meta:
        model=CustomerDetails
        fields=('__all__')
