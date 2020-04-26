from rest_framework import serializers
from .models import Workout, Tag


class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Workout


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Tag
