from rest_framework import generics

from .models import Workout, Tag
from .permissions import IsAuthorOrReadOnly
from .serializers import WorkoutSerializer, TagSerializer


class WorkoutList(generics.ListCreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class WorkoutDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
