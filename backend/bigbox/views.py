from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Box,Activity,Category,Reason
from .serializers import ActivitySerializer, BoxActivitiesSerializer, BoxSerializer, BoxSerializerCustom
from django.shortcuts import render

@api_view(['GET'])
def BoxList(request):
    box = Box.objects.all()
    serializer = BoxSerializer(box, many=True)
    return render(request,'box.html',{"boxList":serializer.data})

@api_view(['GET'])
def getBox(request, pk):
    box = Box.objects.get(id=pk)
    serializer = BoxSerializerCustom(box, many=False)
    return render(request,'boxDetails.html',{"box":serializer.data})

@api_view(['GET'])
def getBoxActivities(request,pk):
    box = Box.objects.get(id=pk)
    serializer = BoxActivitiesSerializer(box, many=False)
    return render(request,'index.htm',{"boxList":serializer.data})

@api_view(['GET'])
def getActivity(request,pk,pkA):
    activity = Activity.objects.get(id=pkA)
    serializer = ActivitySerializer(activity, many=False)
    return Response(serializer.data)

def bootstrap4_index(request):
    return render(request, 'index.html', {})