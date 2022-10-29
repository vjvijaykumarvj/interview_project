from rest_framework import serializers
from.models import Database

class Data_serializer(serializers.ModelSerializer):
    class Meta:
        model = Database
        fields = '__all__'
