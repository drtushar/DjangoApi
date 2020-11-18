from rest_framework import serializers
from . models import Himanshu

class HimanshuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Himanshu
        fields = '__all__'
