from django.urls import path

from .views import WorkoutList, WorkoutDetail, TagList, TagDetail

urlpatterns = [
    path('', WorkoutList.as_view()),
    path('<uuid:pk>/', WorkoutDetail.as_view()),
    path('tags/', TagList.as_view()),
]
