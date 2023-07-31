import paho.mqtt.client as m 
import time 
import random

broker = 'gdv.za.solar-assistant.io'
password = 'admin'
user_name = 'test_test'
broker_address = '192.168.196.144'
port = 1883

def on_connect(client, userdata, flags, rc):
    print('COnnected to MQTT Broker')
    client.subscribe('#')

def on_message(client, userdata, msg):
    print(f'Topic: {msg.topic}')

client = m.Client()

client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(user_name, password)
client.connect(broker, port)

client.loop_start()