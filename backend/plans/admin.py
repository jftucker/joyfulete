from django.contrib import admin

from utils.admin import BaseStackedInline, BaseTabularInline
from workouts.models import Workout
from .models import Day, Week, WeekType, MacroPlan, Plan


class WorkoutInline(BaseStackedInline):
    model = Workout
    extra = 1


class DayInline(BaseTabularInline):
    ordering = ('date',)
    model = Day
    extra = 1
    show_change_link = True


class WeekInline(BaseStackedInline):
    model = Week
    extra = 1


class PlanAdmin(admin.ModelAdmin):
    inlines = [
        WeekInline,
    ]


class DayAdmin(admin.ModelAdmin):
    list_display = ('date', 'id', 'week',)
    ordering = ('date',)

    inlines = [
        WorkoutInline,
    ]


class WeekAdmin(admin.ModelAdmin):
    inlines = [
        DayInline,
    ]


admin.site.register(Day, DayAdmin)
admin.site.register(Week, WeekAdmin)
admin.site.register(WeekType)
admin.site.register(Plan, PlanAdmin)
admin.site.register(MacroPlan)
