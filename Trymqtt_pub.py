import os,json
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
load_dotenv()
client = mqtt.Client()
client.username_pw_set(os.getenv('MQTT_NAME'),os.getenv('MQTT_PW'))
client.connect("127.0.0.1",1883,60)
study = dict()
study = {
    "name":"狗蛋",
    "number":"2",
    "phone_number":"0966666666",
    "sex":"女"
}
study = json.dumps(study,ensure_ascii=False)
print(study)
client.publish("Try/mqtt",study)
