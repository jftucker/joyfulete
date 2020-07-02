from django.contrib import admin

from .models import Activity


class ActivityAdmin(admin.ModelAdmin):
    model = Activity
    list_display = [
        field.name for field in Activity._meta.fields if field.name != 'id']


admin.site.register(Activity, ActivityAdmin)
