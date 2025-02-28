from rest_framework import serializers
from utility.models import JsonfileWater,UploadJsonFiles

class JsonfileWaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = JsonfileWater
        fields = '__all__'
        
class UploadJsonFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadJsonFiles
        fields = '__all__'