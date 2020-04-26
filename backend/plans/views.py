from rest_framework import generics

from .models import Day, Week, Plan, MacroPlan
from .serializers import DaySerializer, WeekSerializer, PlanSerializer, MacroPlanSerializer


class DayList(generics.ListCreateAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer


class DayDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer


class WeekList(generics.ListCreateAPIView):
    queryset = Week.objects.all()
    serializer_class = WeekSerializer


class WeekDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Week.objects.all()
    serializer_class = WeekSerializer

class PlanList(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class PlanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class MacroPlanList(generics.ListCreateAPIView):
    queryset = MacroPlan.objects.all()
    serializer_class = MacroPlanSerializer


class MacroPlanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MacroPlan.objects.all()
    serializer_class = MacroPlanSerializer