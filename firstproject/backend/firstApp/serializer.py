from rest_framework import serializers

from .models import userDetails

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = userDetails
        fields = ('id', 'name', 'state','district','shop_name','mobilenumber','emailId','password')