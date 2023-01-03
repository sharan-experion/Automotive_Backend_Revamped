from rest_framework import serializers

from .models import category,products

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ('id', 'categoryname',)

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=products
        fields=('__all__')
