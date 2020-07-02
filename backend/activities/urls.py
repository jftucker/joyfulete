from django.urls import path

from .views import upload_from_csv, ActivityList, ActivityDetail

urlpatterns = [
    path('csvupload/', upload_from_csv, name='activities_bulk_upload'),
    path('', ActivityList.as_view()),
    path('<uuid:pk>/', ActivityDetail.as_view()),
]
