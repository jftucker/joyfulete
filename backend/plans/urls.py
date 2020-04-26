from django.urls import path

from .views import (
    DayList,
    DayDetail,
    WeekList, 
    WeekDetail, 
    PlanList, 
    PlanDetail, 
    MacroPlanList,
    MacroPlanDetail,
) 

urlpatterns = [
    path('days/', DayList.as_view()),
    path('days/<uuid:pk>/', DayDetail.as_view()),
    path('weeks/', WeekList.as_view()),
    path('weeks/<uuid:pk>/', WeekDetail.as_view()),
    path('', PlanList.as_view()),
    path('<uuid:pk>/', PlanDetail.as_view()),
    path('macroplans/', MacroPlanList.as_view()),
    path('macroplans/<uuid:pk>/', MacroPlanDetail.as_view()),
]
