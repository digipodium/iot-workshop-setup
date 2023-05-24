from machine import Pin, ADC
from time import sleep
import network
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect("Actnet2", ". .qwaszx12")
print("wifi connected", station.isconnected())
print("wifi config", station.ifconfig())
led = Pin(2, Pin.OUT)
ldr = ADC(0)

while True:
  v = ldr.read()
  print(">>>", v)
  if v > 150:
    led.on() # off for pin 2
  else:
    led.off() # on 
  sleep(.25)

