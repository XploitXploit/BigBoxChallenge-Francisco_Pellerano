
from django.urls import path, include
from django.conf.urls import url
from .views import BoxList, getActivity,getBox, getBoxActivities, getBoxSlug, homeView

urlpatterns = [
    path(r'', homeView,name="home"),
    path('box/', BoxList, name="boxList"),
    path('box/<int:pk>/',getBox,name='boxId'),
    path('box/<str:_slug>/',getBoxSlug,name='boxSlug'),
    path('box/<int:pk>/activity/',getBoxActivities,name='boxActivities'),
    path('box/<int:pk>/activity/<int:pkA>/',getActivity,name='boxActivitiesId'),
]
