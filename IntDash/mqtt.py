import paho.mqtt.client as mqtt
import threading
import json


class MQTT:
    
    def __init__(self):
        print("started initialising")
        mqttIp = '127.0.0.1'
        MQTT.mqtt_subscriber = mqtt.Client('Live Lab')
        MQTT.mqtt_subscriber.on_message = MQTT.on_message
        MQTT.mqtt_subscriber.connect(mqttIp, 1883, 70)
        MQTT.mqtt_subscriber.subscribe('#', 0)

        MQTT.threadSubscriber = threading.Thread(target=self.startLoopingSubscriber)
        MQTT.threadSubscriber.start()
        print("end initialising")
        
        
    def on_message( client, userdata, message):
        print( str(message.payload.decode("utf-8")))
        mesg_topic = message.topic
        
        if "sensor/" in mesg_topic:
            print(mesg_topic)
            mesg_topic=mesg_topic.replace("sensor/",'')
            print(mesg_topic, type(mesg_topic))
        file_name = "Files/"+mesg_topic+".txt"
        print(file_name)
        try:
            f = open(file_name, "w")
            f.write(str(message.payload.decode("utf-8")))
        except (IOError, FileNotFoundError) as error:
            print("no subscription")
        
        #    file_name = "Files/temperature_sensor.txt"
        #    f = open(file_name, "w")
        #    f.write(str(message.payload.decode("utf-8")))
        #    
        #elif (message.topic =='sensor/sun_light'):
        #    file_name = "Files/sunlight_sensor.txt"
        #    f = open(file_name, "w")
        #    f.write(str(message.payload.decode("utf-8")))
        #    
        #elif (message.topic =='sensor/washbasin_light'):
        #    file_name = "Files/washbasin_light.txt"
        #    f = open(file_name, "w")
        #    f.write(str(message.payload.decode("utf-8")))
        #    
        #elif (message.topic =='sensor/room_light1'):
        #    file_name = "Files/room_light1.txt"
        #    f = open(file_name, "w")
        #    f.write(str(message.payload.decode("utf-8")))
        
        
        
    def startLoopingSubscriber(self):
        print("started looping")
        MQTT.mqtt_subscriber.loop_forever()
        print("stopped looping")
        
#if __name__ == "__main__":
#    mqtt = MQTT()
#    
