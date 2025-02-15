from django.urls import path
from . import views

urlpatterns=[
    path('check-geofence/',views.check_geofence,name='check_geofence'),
    path('check-in/', views.check_in_view, name='check_in'),
]