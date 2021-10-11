import json
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django.http import JsonResponse

url = "http://localhost:8123/api/services/"

headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIzYTBhZWIwZjVmZjE0MzkwYWE4YjVlN2ZmYTg0NDU4MiIsImlhdCI6MTYzMzk1OTg1OCwiZXhwIjoxOTQ5MzE5ODU4fQ.yXJe76bpJOUPsJB8YQTQzWkKmnSBf7BXlrQHc99AMYA",
    "content-type": "application/json",
}

# Create your views here.
def room1_display(request):
    return render(request, 'room1.html')

    
def getSensorData(request):
    print("in get sensor data")
    file_sunlight_sensor = "Files/" + "sunlight_sensor" + ".txt"
    file_temperature_sensor = "Files/" + "temperature_sensor" + ".txt"
    file_washbasin_light = "Files/" + "washbasin_light" + ".txt"
    file_room_light1 = "Files/" + "room_light1" + ".txt"
    file_bot = "Files/bot.txt"
    
    data_sunlight_sensor = open(file_sunlight_sensor, "r").readline()
    data_temperature_sensor = open(file_temperature_sensor, "r").readline()
    data_washbasin_light = open(file_washbasin_light, "r").readline()
    data_room_light1 = open(file_room_light1, "r").readline()
    data_bot = open(file_bot, "r").readlines()
    
    f = {
          "sunlight_sensor": data_sunlight_sensor, 
          "temperature_sensor" : data_temperature_sensor,
          "washbasin_light" : data_washbasin_light,
          "room_light1" : data_room_light1,
          "bot":{
                "left": data_bot[0],
                "bottom": data_bot[1]}
          }
    print(f)
    return JsonResponse(json.dumps(f, ensure_ascii=False), safe=False)
    
    
def sendActorDataRoomLight(request):
    print("in herre")
    url_roomlight = url + "input_boolean/toggle"
    entity_data = {"entity_id" : "input_boolean.room_light1" }
    
    response =  requests.post(url_roomlight, headers=headers, data = json.dumps(entity_data))
    print (response.text)
    return render(request, 'room1.html')
    
def sendActorDataWashLight(request):
    url_washlight = url + "input_boolean/toggle"
    entity_data = {"entity_id" : "input_boolean.washbasin_light" }
    
    response =  requests.post(url_washlight, headers=headers, data = json.dumps(entity_data))
    print (response.text)
    return render(request, 'room1.html')
    
    


    
