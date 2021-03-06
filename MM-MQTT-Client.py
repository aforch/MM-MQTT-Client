# Simple MQTT client script intended for controlling raspberry pi display
# Heavily based upon examples from Eclipse Paho MQTT Python Client
# See https://github.com/eclipse/paho.mqtt.python for more information on library and examples
#

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
from subprocess import call
from configparser import ConfigParser
import os

#Config file setup and read
config = ConfigParser(delimiters=('=', ))
config.optionxform = str
config.read('MM-MQTT.ini')
auth = {'username':config.get('broker','mqtt_user'), 'password':config.get('broker','mqtt_passwd')}
topics = {'status':config.get('mqtt_topic','status_topic'), 'set':config.get('mqtt_topic','set_topic')}
broker = {'host':config.get('broker','mqtt_server'),'port':int(config.get('broker','mqtt_port'))}
retainFlag = True
    
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(config.get('mqtt_topic', 'set_topic'))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(str(msg.payload))
    if 'ON' in str(msg.payload):
        try:
            call(['vcgencmd', 'display_power', '1'])
            update_status("ON")
            #print("On")
        except:
            update_status("OFF")
    elif "OFF" in str(msg.payload):
        try:
            call(['vcgencmd', 'display_power', '0'])
            update_status("OFF")
            #print("Off")
        except:
            update_status("ON")
            
# Publish back 
def update_status(status):
    publish.single(topics['status'], status, retain=retainFlag, hostname=broker['host'] ,auth=auth)
   
        
if __name__== "__main__":
    
    
    #MQTT Client setup
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(auth['username'], auth['password'])

    #MQTT Connection and loop
    client.connect(broker['host'], broker['port'], 60)

    client.loop_forever()

    