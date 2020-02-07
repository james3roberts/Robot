##This program is to get the motor to run. 


#first set up the motor to run/
import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#if these do not work try 17,12,27,22
control.pins = [17,18,27,22]
for pin in StepPins:
  print('Setup pins')
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, False)
  #improvement have been made from old code. runs much better. 
Seq = [
  [1,0,0,1],
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1]
]
StepCount = len(Seq)
StepDir = 2
if len (sys.argv)>1:
  WaitTime = int(sys.argv[1])/float(1000)
else:WaitTime = 10/float(1000)
StepCounter = 0
while True:
  print(StepCount, )
  print(Seq[StepCounter])

  for pin in range(0,4):
    xpin = StepPins[pin]
    if Seq[StepCounter][pin] !=0:
    print('Enable GPIO%1'%(xpin))
    GPIO.output(xpin, True)
  else:
    GPIO.output(xpin, False)
  StepCounter += StepDir
  if (StepCounter>= StepCount):
    StepCounter = 0
  if(StepCounter <0):
    StepCounter = StepCount + StepDir
  time.sleep(WaitTime)

