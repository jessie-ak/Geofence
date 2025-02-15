from django.shortcuts import render
from django.http import  JsonResponse
import json 
from .models import Geofence
from math import radians,sin,cos,sqrt,atan2 
# Create your views here.

def haversine(lat1,lon1,lat2,lon2):
    R=6371
    dlat=radians(lat2-lat1)
    dlon=radians(lon2-lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c=2*atan2(sqrt(a),sqrt(1-a))
    return R*c 

def check_in_view(request):
    return render(request, 'main/geofence.html')

def check_geofence(request):
    if request.method=='POST':
        data = json.loads(request.body)
        user_lat = float(data['latitude'])
        user_lon = float(data['longitude'])

        

        geofences=Geofence.objects.all()
        for geofence in geofences:
            distance= haversine(user_lat, user_lon,geofence.latitude,geofence.longitude)
            print(f"Received coordinates: Latitude={user_lat}, Longitude={user_lon}")
            print(f"Calculated Distance: {distance} km")
            print(f"Geofence Center: Latitude={geofence.latitude}, Longitude={geofence.longitude}")
        
            if distance<=geofence.radius:
                return JsonResponse({'inside':True, 'geofence':geofence.name})
            
        return JsonResponse({'inside':False})
    else:   
        return JsonResponse({'error':'Invalid request'},status=400)