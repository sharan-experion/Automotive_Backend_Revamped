from rest_framework import serializers
from .models import tbl_Employee


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=tbl_Employee
        fields=('__all__')
