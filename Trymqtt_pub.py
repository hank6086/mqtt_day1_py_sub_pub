import os
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import json
load_dotenv()
client = mqtt.Client()
client.username_pw_set(os.getenv('MQTT_NAME'),os.getenv('MQTT_PW'))
client.connect("127.0.0.1",1883,60)

study = {
    "name":"狗蛋香腸",
    "number":"20",
    "phone_number":"0912345678",
}
study = json.dumps(study,ensure_ascii=False)
print(study)
client.publish("Try/mqtt",study,)
