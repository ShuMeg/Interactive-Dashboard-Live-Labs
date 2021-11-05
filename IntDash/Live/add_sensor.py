#
#Add sensor to the html file and communicate
#to the Home Assistant. Also get live updates
#from sensor to the html page
#
#


# import GeeksModel from models.py
from .models import newResource



def getSensorList():

    all_entries = newResource.objects.filter(resource = "sensor")
    sensor_list = []
    print("entries:")
    for i in all_entries:
        sensor = {"sensor" : i.name,
                  "posx" : i.position_x,
                  "posy" : i.position_y}
        sensor_list.append(sensor)

    return (sensor_list)

def getBotList() :
    all_entries = newResource.objects.filter(resource = "bot")
    bot_list = []
    print("entries:")
    for i in all_entries:
        bot = {"bot" : i.name,
                  "posx" : i.position_x,
                  "posy" : i.position_y}
        bot_list.append(bot)
        
    return (bot_list)
    
def delSensor(sensor):
    print("in delete sensor"+str(sensor))
    newResource.objects.get(name=str(sensor)).delete()
    print ("deleted")
    
    
def getActuatorList() :
    all_entries = newResource.objects.filter(resource = "actuator")
    actuator_list = []
    print("entries:")
    for i in all_entries:
        actuator = {"actuator" : i.name,
                  "posx" : i.position_x,
                  "posy" : i.position_y}
        actuator_list.append(actuator)
        
    return (actuator_list)

    
def delActuator(actuator):    
    newResource.objects.get(name=str(actuator)).delete()
    
    

