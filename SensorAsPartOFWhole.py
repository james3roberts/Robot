##This program is to get the motor to run. 
##Made on 2/5/20 Might need improved. found on medium. 

#first set up the motor to run/
import sys
import PRi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#if these do not work try 17,12,27,22
control.pins = [11,12,13,15]
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]
for i in range(512):
  for halfstep in range(8):
    for pin in range(4):
      GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
    time.sleep(0.001)
GPIO.cleanup()