import os
import paho.mqtt.client as mqtt
client = mqtt.Client()
client.username_pw_set(os.getenv('MQTT_NAME'),os.getenv('MQTT_PW'))
client.connect("192.168.1.101",1883,60)

test = "Hellol"
print(test)
client.publish("Try/mqtt",test)
