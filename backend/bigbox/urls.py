
from django.urls import path, include
from django.conf.urls import url
from .views import BoxList, getActivity,getBox, getBoxActivities,bootstrap4_index

urlpatterns = [
    path(r'', bootstrap4_index, name="index"),
    path('box/', BoxList, name="boxList"),
    path('box/<str:pk>/',getBox,name='boxId'),
    path('box/<str:pk>/activity/',getBoxActivities,name='boxActivities'),
    path('box/<str:pk>/activity/<str:pkA>/',getActivity,name='boxActivities'),
]
