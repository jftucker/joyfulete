from django.urls import path

from .views import UserList, UserDetail, ProfileList, ProfileDetail

urlpatterns = [
    path('', UserList.as_view()),
    path('<uuid:pk>/', UserDetail.as_view()),
    path('profiles/', ProfileList.as_view()),
    path('<uuid:pk>/profile/', ProfileDetail.as_view()),
]
