import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django.http import JsonResponse


# Create your views here.
def room1_display(request):
    return render(request, 'room1.html')
    
def room2_display(request):
    return render(request, 'room2.html')

def requestroom(request):
    return render(request, 'room1.html')
    
def getSensorData(request):
    print("in get sensor data")
    file_name = "Files/" + "sunlight_sensor" + ".txt"
    data = open(file_name, "r").readline()
    f = {"sunlight_sensor": data}
    print(f)
    return JsonResponse(json.dumps(f, ensure_ascii=False), safe=False)
    
    
    


    