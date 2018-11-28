# Simple MQTT client script intended for controlling raspberry pi display
# Heavily based upon examples from Eclipse Paho™ MQTT Python Client
# See https://github.com/eclipse/paho.mqtt.python for more information on library and examples
#

import paho.mqtt.client as mqtt
from subprocess import call

#actual username, password, MQTT server address, and topic here
mqtt_name = "user" 
mqtt_pass = "password"
mqtt_server = "1.2.3.4"
mqtt_topic = "home/my_topic"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(mqtt_topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(str(msg.payload))
    if 'ON' in str(msg.payload):
        #call(['vcgencmd', 'display_power', '0'])
        print("On")
    elif "OFF" in str(msg.payload):
        #call(['vcgencmd', 'display_power', '1'])
        print("Off")

        
if __name__== "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(mqtt_name, mqtt_pass)

    client.connect(mqtt_server, 1883, 60)


    client.loop_forever()

    