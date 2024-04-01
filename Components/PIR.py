from time import sleep
import RPi.GPIO as GPIO

led = 5
# pin 11 先可以正常用來 input, pin 3 要上拉成 1
pir = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(led, GPIO.OUT)
GPIO.output(led, False)
GPIO.setup(pir, GPIO.IN)

moved = 0
coolDownTime = 0
lightTurnOnTime = 6;

sleep(2) #give sensor to startup

print("Start")
try:
  while True:
    moved = GPIO.input(pir)

    if moved == 0:
      if coolDownTime <= 0:
        print("Motion detected!")
      coolDownTime = lightTurnOnTime  # turn on LED 

    if coolDownTime > 0:
      GPIO.output(led, True)
    else:
      GPIO.output(led, False)         # everytime detect will reset the cool down time

    sleep(0.1)
    coolDownTime -= 0.1
    print(coolDownTime)

finally:
  print("\nExit the program...")
  GPIO.cleanup()
