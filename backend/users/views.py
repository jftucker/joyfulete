from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
