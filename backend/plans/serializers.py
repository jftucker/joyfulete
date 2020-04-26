from rest_framework import serializers
from .models import Day, Week, WeekType, Plan, MacroPlan

from workouts.serializers import WorkoutSerializer


class DaySerializer(serializers.ModelSerializer):
    workouts = WorkoutSerializer(many=True)

    class Meta:
        model = Day
        fields = '__all__'  # ('workouts',)


class WeekSerializer(serializers.ModelSerializer):
    days = DaySerializer(many=True)

    class Meta:
        model = Week
        fields = '__all__'


class WeekTypeSerializer(serializers.ModelSerializer):
    weeks = WeekSerializer(many=True)

    class Meta:
        models = WeekType
        fields = '__all__'


class PlanSerializer(serializers.ModelSerializer):
    weeks = WeekSerializer(many=True)

    class Meta:
        model = Plan
        fields = '__all__'


class MacroPlanSerializer(serializers.ModelSerializer):
    weeksFramework = WeekTypeSerializer(many=True)

    class Meta:
        model = MacroPlan
        fields = '__all__'
