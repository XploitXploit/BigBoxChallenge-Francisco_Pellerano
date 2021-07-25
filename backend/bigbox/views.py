
from rest_framework.decorators import api_view
from .models import Box,Activity
from .serializers import  BoxSerializer, BoxSerializerCustom
from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

#View for listing the box's
@api_view(['GET'])
def BoxList(request):
    box = Box.objects.all()
    serializer = BoxSerializer(box, many=True)
    return render(request,'box.html',{"boxList":serializer.data})
#View for listing a box by id
@api_view(['GET'])
def getBox(request, pk):
    box = Box.objects.get(id=pk)
    serializer = BoxSerializerCustom(box, many=False)
    return render(request,'boxDetails.html',{"box":serializer.data})
#Paginated view for listing the box activities 
@api_view(['GET'])
def getBoxActivities(request,pk):
    box = Box.objects.get(id=pk)

    paginator = Paginator(box.activities.values(),20)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)  
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    context = {'page_obj': page_obj, 'box':box}

    return render(request,'boxActivities.html',context)
#View for activitiDetails
@api_view(['GET'])
def getActivity(request,pk,pkA):
    box = Box.objects.get(id=pk)
    activity = Activity.objects.get(id=pkA)

    context={'activity': activity, 'box':box}
    return render(request,'activityDetail.html',context)
#View for serching by slug
@api_view(['GET'])
def getBoxSlug(request,_slug):
    box = Box.objects.get(Q(slug__startswith=_slug))
    serializer = BoxSerializerCustom(box, many=False)
    context = {"box":serializer.data}
    
    return render(request,'boxDetails.html',context)

@api_view(['GET'])
def homeView(request):
    return render(request,'home.html')