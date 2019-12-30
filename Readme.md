# MM-MQTT-Client

H5 What's it do? 
MM-MQTT-Client started as (and still very much is) a basic mqtt client for raspberry pi with the primary objective of turning the display on and off via mqtt messages.

H5 Why's it called MM-MQTT-Client? 
I was originally running magic mirror on this particular raspberry pi, and therefore the naming convention matched that of the magic mirror modules. 

H5 How does it work? 
Basically, like this:
1. Add your mqtt broker info and topic info to the ini file
2. Run the python script and make sure it executes properly
3. Register your service to run at startup using the provided service template and the instructions [here](https://www.raspberrypi.org/documentation/linux/usage/systemd.md "Raspberry Pi Systemd Page")
4. Extra Bonus: Add to HomeAssistant using the provided configuration template

H5 To-Do
Add ability to handle multiple mqtt topics and/or add the ability to pass commands to run
