import time
import RPi.GPIO as GPIO

GPIO_TRIGGER = 3
GPIO_ECHO    = 17 # 4 not work

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#
# 如果用 GPIO.setmode(GPIO.BOARD) 不知為何會出 Error, 轉 GPIO.BIM 就好
# ValueError: The channel sent is invalid on a Raspberry Pi

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def getDistance():
  GPIO.output(GPIO_TRIGGER, False)
  time.sleep(0.5)
  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()
  while GPIO.input(GPIO_ECHO) == 0:
    start = time.time()
  while GPIO.input(GPIO_ECHO) == 1:
    stop = time.time()
  elapsed = stop - start
  distance = elapsed * 34300
  distance = distance / 2
  return distance

#main program
print("Ultrasonic Measurement")
try:
  while 1:
    cm = getDistance()
    print("Distance : %.1f cm" % cm)
    time.sleep(1)
finally:
  GPIO.cleanup()
  print("\nEnd")
