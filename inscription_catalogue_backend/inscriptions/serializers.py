from rest_framework import routers,serializers,viewsets
from .models import *

class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = '__all__'

class InscriptionPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InscriptionPhoto
        fields = '__all__'

class WritingScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = WritingScript
        fields = ['id','name']

class MediumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medium
        fields = ['id','name']