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

    context['form']= form
    
    return render(request, 'room1.html', context)

def getSensorData(request):
    sensorData = {}
    sensors_list = getSensorList()
    actuator_list = getActuatorList()
    bot_list = getBotList()
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
    
    for bot in bot_list:
        try:
            sensor_file_name = "Files/" + bot["bot"] + ".txt"
            file = open(sensor_file_name, "r")
            str = file.readlines()
            str[0] = str[0].rstrip("\n")
            str[1] = str[1].rstrip("\n")
            sensorData[bot["bot"]] = str
        except (IOError, FileNotFoundError) as error:
            file = open(sensor_file_name, "w")
            sensorData[bot["bot"]] = ""
        finally:
            file.close() 
            
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

def reloadData(request):
    resource_list = {}
    resource_list["sensors"] = getSensorList()
    resource_list["actuators"] = getActuatorList()
    resource_list["bot"] = getBotList()
    return JsonResponse(json.dumps(resource_list, ensure_ascii=False), safe=False)

