from rest_framework import serializers
from utility.models import JsonfileWater

class JsonfileWaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = JsonfileWater
        fields = '__all__'
