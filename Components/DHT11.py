""" install Component Library
sudo apt-get update
sudo apt-get install python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel
sudo pip3 install Adafruit_DHT
"""

import sys
import time
import Adafruit_DHT

sensor  = Adafruit_DHT.DHT11  # 第 pin 7 
GPIOpin = 4

while True:
  humidity, temperature = Adafruit_DHT.read_retry(sensor, GPIOpin)  # set pin，每次 get 都要
  # humidity, temperature = Adafruit_DHT.read(sensor, GPIOpin)
  if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}C  Humidity={1:0.1f}%'.format(temperature, humidity))
  else:
    print('Failed to get reading. Try again!')
  time.sleep(2)
