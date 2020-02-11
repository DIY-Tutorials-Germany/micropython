from machine import Pin
from time import sleep

# ESP32 GPIO 26
#relay = Pin(26, Pin.OUT)
#led = Pin(2, Pin.OUT)

# ESP8266 GPIO 5 D1
relay = Pin(5, Pin.OUT)
led = Pin(2, Pin.OUT)

while True:
  # RELAY ON
  relay.value(0)
  led.value( 0)
  sleep(5)
  # RELAY OFF
  relay.value(1)
  led.value(1)
  sleep(5)
