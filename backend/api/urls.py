from django.urls import path, include

urlpatterns = [
    path('workouts/', include('workouts.urls')),
    path('users/', include('users.urls')),
    path('plans/', include('plans.urls')),
]
