import paho.mqtt.client as mqtt
import threading
import json


class MQTT:
    
    def __init__(self):
        print("started initialising")
        mqttIp = 'localhost'
        MQTT.mqtt_subscriber = mqtt.Client('Live Lab')
        MQTT.mqtt_subscriber.on_message = MQTT.on_message
        MQTT.mqtt_subscriber.connect(mqttIp, 1883, 70)
        MQTT.mqtt_subscriber.subscribe("temperature_sensor", 2)
        MQTT.mqtt_subscriber.subscribe("sunlight_sensor", 2)
        
        threadSubscriber = threading.Thread(target=self.startLoopingSubscriber)
        threadSubscriber.start()
        print("end initialising")
        
        
    def on_message( client, userdata, message):
        print( str(message.payload.decode("utf-8")))
        #messageJson = json.loads(message.payload.decode())
        file_name = "Files/" + message.topic + ".txt"
        f = open(file_name, "w")
        f.write(str(message.payload.decode("utf-8")))
        #if message.topic == "changeGreen":
        #    f = open("Files/changeGreen.txt", "w")
        #    f.write(str(message.payload.decode("utf-8")))
        #    
        #if message.topic
        
        
    def startLoopingSubscriber(self):
        print("started looping")
        MQTT.mqtt_subscriber.loop_forever()
        print("stopped looping")