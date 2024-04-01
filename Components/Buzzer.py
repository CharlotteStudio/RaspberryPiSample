import RPi.GPIO as GPIO

buzzerPin = 35

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzerPin, GPIO.OUT)

for r in range(1000):
  for x in range(250):
    GPIO.output(buzzerPin, 1)
  for x in range(250):
    GPIO.output(buzzerPin, 0)