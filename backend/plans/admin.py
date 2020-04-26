"""Configures general plan administration
"""
from django.contrib import admin

from utils.admin import BaseStackedInline, BaseTabularInline
from workouts.models import Workout
from .models import Day, Week, WeekType, MacroPlan, Plan


class WorkoutInline(BaseStackedInline):
    """Configures inlines for workout model to be used by foreign keys

    Arguments:
        BaseStackedInline {class} -- wraps admin.StackedInline with project modifications
    """
    model = Workout
    extra = 1


class DayInline(BaseTabularInline):
    """Configures inlines for day model to be used by foreign keys

    Arguments:
        BaseStackedInline {class} -- wraps admin.StackedInline with project modifications
    """
    fields = ('date',)
    ordering = ('date',)
    model = Day
    extra = 1
    show_change_link = True


class WeekInline(BaseStackedInline):
    """Configures inlines for week model to be used by foreign keys

    Arguments:
        BaseStackedInline {class} -- wraps admin.StackedInline with project modifications
    """
    model = Week
    extra = 1


class PlanAdmin(admin.ModelAdmin):
    """Configures Plan Administration

    Arguments:
        admin {class} -- django base administration
    """
    inlines = [
        WeekInline,
    ]


class DayAdmin(admin.ModelAdmin):
    """Configures Day Administration

    Arguments:
        admin {class} -- django base administration
    """
    list_display = ('date', 'id', 'week')
    ordering = ('date',)

    inlines = [
        WorkoutInline,
    ]


class WeekAdmin(admin.ModelAdmin):
    """Configures Week Administration

    Arguments:
        admin {class} -- django base administration
    """
    inlines = [
        DayInline,
    ]


admin.site.register(Day, DayAdmin)
admin.site.register(Week, WeekAdmin)
admin.site.register(WeekType)
admin.site.register(Plan, PlanAdmin)
admin.site.register(MacroPlan)
