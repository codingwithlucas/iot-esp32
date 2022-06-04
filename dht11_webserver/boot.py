from time import sleep
from dht import DHT11
from network import WLAN, STA_IF
from esp import osdebug
from gc import collect
from machine import Pin
import socket

led = Pin(2, Pin.OUT)
sensor = DHT11(Pin(14))
# Wifi credentials
wifi_name = "YOUR_WIFI_NAME"
wifi_password = "YOUR_WIFI_PASSWORD"
# Turning wifi on and connecting to the network
station = WLAN(STA_IF)
station.active(True)
station.connect(wifi_name, wifi_password)

while station.isconnected() == False:
    # This loop keeps going until ESP32 connects to wifi
    pass

print("ESP32 has been connected to wifi")
print(station.ifconfig())
# The onboard led blinks 5 times to indicate ESP32 is connected to wifi
for i in range(0, 5):
    led.value(True)
    sleep(0.100)
    led.value(False)
    sleep(0.100)