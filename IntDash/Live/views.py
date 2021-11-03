import os
import sys
import json
import requests
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django.http import JsonResponse
from .forms import newResourceForms
from .models import newResource
from .add_sensor import *


url = "http://localhost:8123/api/services/"

headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIzYTBhZWIwZjVmZjE0MzkwYWE4YjVlN2ZmYTg0NDU4MiIsImlhdCI6MTYzMzk1OTg1OCwiZXhwIjoxOTQ5MzE5ODU4fQ.yXJe76bpJOUPsJB8YQTQzWkKmnSBf7BXlrQHc99AMYA",
    "content-type": "application/json",
}

# Create your views here.
def room1_display(request):
    context={}
    name = ""
    form = newResourceForms()
    if request.method == "POST":
       pDict = request.POST.copy() 
       form = newResourceForms(pDict) #if not valid shows error with previous post values in corresponding field
       if form.is_valid():
           form.save()
           name = form.cleaned_data.get("name")
           posx = form.cleaned_data.get("position_x")
           posy = form.cleaned_data.get("position_y")
           
           #form = newResourceForms() # show empty form no need to give HttpResponseRedirect()
           
       
    #form=newResourceForms(request.POST or None, request.FILES or None)
    #if form.is_valid():
    #   form.save()
    #   name = form.cleaned_data.get("name")
    #   posx = form.cleaned_data.get("position_x")
    #   posy = form.cleaned_data.get("position_y")
    #   getSensorList(name, posx, posy)
    #   form=newResourceForms(request.POST or None, request.FILES or None)
    context['form']= form
    
    return render(request, 'room1.html', context)
    
    
def getSensorData(request):
    sensorData = {}
    sensors_list = getSensorList()
    actuator_list = getActuatorList()
    for sensors in sensors_list:
        try:
            sensor_file_name = "Files/" + sensors["sensor"] + ".txt"
            file = open(sensor_file_name, "r")
            sensorData[sensors["sensor"]] =  file.readline()
        except (IOError, FileNotFoundError) as error:
            file = open(sensor_file_name, "w")
            sensorData[sensors["sensor"]] = ""
        finally:
            file.close()
            
    for actuator in actuator_list:
        try:
            sensor_file_name = "Files/" + actuator["actuator"] + ".txt"
            file = open(sensor_file_name, "r")
            sensorData[actuator["actuator"]] =  file.readline()
        except (IOError, FileNotFoundError) as error:
            file = open(sensor_file_name, "w")
            sensorData[actuator["actuator"]] = ""
        finally:
            file.close()    
    
    sensorData["washbasin_light"] = open("Files/washbasin_light.txt", "r").readline()
    sensorData["room_light1"] = open("Files/room_light1.txt", "r").readline()
    print("in get sensor datac: ")
    print(sensorData)
    return JsonResponse(json.dumps(sensorData, ensure_ascii=False), safe=False)

def getActuatorData(request):
    actuatorData = {}
    actuators_list = getActuatorList()
    for actuators in actuators_list:
        try:
            actuator_file_name = "Files/" + actuators["actuator"] + ".txt"
            file = open(sensor_file_name, "r")
            sensorData[actuators["actuator"]] =  file.readline()
        except (IOError, FileNotFoundError) as error:
            file = open(sensor_file_name, "w")
            sensorData[actuators["actuator"]] = ""
        finally:
            file.close()

    print("in get actuator data")
    return JsonResponse(json.dumps(sensorData, ensure_ascii=False), safe=False)

def deleteSensorData(request):
    sensor_name = request.POST.get('sensorName')
    delSensor(sensor_name)
    sensor_file_name = "Files/" + sensor_name + ".txt"
    return JsonResponse({'message':'success'},status=200)

def clickActuator(request):
    actuator = request.POST.get('actuatorName')
    url_switchActuator = url + "input_boolean/toggle"
    entity_data = {"entity_id" : "input_boolean."+actuator }
    response =  requests.post(url_switchActuator, headers=headers, data = json.dumps(entity_data))
    return JsonResponse({'message':'success'}, status=200)

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
    
    
def reloadData(request):
    resource_list = {}
    resource_list["sensors"] = getSensorList()
    resource_list["actuators"] = getActuatorList()
    return JsonResponse(json.dumps(resource_list, ensure_ascii=False), safe=False)

