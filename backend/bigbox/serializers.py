from django.db import models
from rest_framework import  serializers
from .models import Box,Activity,Category,Reason
from bs4 import BeautifulSoup



class BoxSerializer(serializers.ModelSerializer):
    class Meta:
       model = Box
       #fields = '__all__'
       fields = ["id","name","internal_name","description","price","purchase_available","category","activities"]
    
class BoxSerializerCustom(serializers.ModelSerializer):
    activities = serializers.SerializerMethodField(read_only=True)
    class Meta:
       model = Box
       #fields = '__all__'
       fields = ["id","name","internal_name","description","price","purchase_available","category","activities"]

    def get_activities(self,obj):
        items= obj.activities.all()[0:5]
        serializer = ActivitySerializer(items,many=True)
        return serializer.data
    

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id','name','internal_name',"description",'category','reasons','purchase_available']
    

class BoxActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
       model = Box
       #fields = '__all__'
       fields = ["activities",]
    
