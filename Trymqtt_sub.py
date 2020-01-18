import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os
load_dotenv()
def on_connect(client,userdata,flags,rc):# 當地端程式連線伺服器得到回應時，要做的動作
    print("Connect with result code" + str(rc))
    client.subscribe("Try/mqtt")
    # 將訂閱主題寫在on_connet中
    # 如果我們失去連線或重新連線時 
    # 地端程式將會重新訂閱
def on_messqge(client,userdata,msg):
    print(msg.topic  +  " " + msg.payload.decode('utf-8'))
    #轉換編碼utf-8

client = mqtt.Client()

client.on_connect = on_connect

client.on_messqge = on_messqge

client.username_pw_set(os.getenv('MQTT_NAME'),os.getenv('MQTT_PW'))

client.Connect = ("192.168.1.101",1883,60)

client.loop_forever()
