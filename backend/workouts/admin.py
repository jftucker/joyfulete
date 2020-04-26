from django.contrib import admin

from .models import Workout, Tag

class TagInline(admin.TabularInline):
    model = Tag.workouts.through


class WorkoutAdmin(admin.ModelAdmin):
    inlines = [
        TagInline,
    ]
    list_display = ["title", "description",]

class TagAdmin(admin.ModelAdmin):
    exclude = ('workouts',)

admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Tag, TagAdmin)