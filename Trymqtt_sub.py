import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os,pymysql,json
load_dotenv()
db = pymysql.connect("localhost",os.getenv('MYSQL_USER'),os.getenv('MYSQL_PW'),"Trymqtt")
cursor = db.cursor()
def on_connect(client,userdata,flags,rc):# 當地端程式連線伺服器得到回應時，要做的動作
    print("Connect with result code" + str(rc))
    client.subscribe("Try/mqtt")
    # 將訂閱主題寫在on_connet中
    # 如果我們失去連線或重新連線時 
    # 地端程式將會重新訂閱
def on_message(client,userdata,msg):
    meg = json.loads(msg.payload,encoding="GBK2312")
    #轉換編碼utf-8
    work="INSERT INTO classmate(name,number,phone_number,sex)VALUES('%s','%s','%s','%s');"%(meg["name"],meg["number"],meg["phone_number"],meg["sex"])
    # work="INSERT INTO classmate(name,number,phone_number,sex)VALUES('" + meg["name"] + "','" + meg["number"] + "','" + meg["phone_number"] + "','" + meg["sex"] + "');"
    print(work)
    try:
        cursor.execute(work)
        db.commit()
    except:
        db.rollback()
    db.close()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(os.getenv('MQTT_NAME'),os.getenv('MQTT_PW'))
client.connect("127.0.0.1",1883,60)
client.loop_forever()



