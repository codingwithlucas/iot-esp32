# This file is executed on every boot (including wake-boot from deepsleep)
try:
    import usocket as socket
except:
    import socket

# Allow us to use the GPIOs
from machine import Pin
# It is used to connect ESP to a (wi-fi) network
import network
import esp
import gc

# Deactivate vendor OS debugging messages
esp.osdebug(None)
# Garbage collector
gc.collect()

wifi_name = "YOUR WIFI NAME"
password =  "YOUR WIFI PASSWORD"
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(wifi_name, password)

while station.isconnected() == False:
    pass

print("Connected to wifi")
print(station.ifconfig())

redLed = Pin(18, Pin.OUT)
greenLed = Pin(19, Pin.OUT)
blueLed = Pin(21, Pin.OUT)