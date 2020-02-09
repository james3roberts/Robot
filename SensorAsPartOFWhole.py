##This program is to get the motor to run. 
##Stepper.py is the code i use to update this off of the pi


#first set up the motor to run/
import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#had the wrong variable called
StepPins = [17,18,27,22]
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

      #the print line does not work and I think that is breaking the code
      
      print('Enable GPIO%1' %(xpin))
      GPIO.output(xpin, True)
  else:
    GPIO.output(xpin, False)
  StepCounter += StepDir
  if (StepCounter>= StepCount):
    StepCounter = 0
  if(StepCounter <0):
    StepCounter = StepCount + StepDir
  time.sleep(WaitTime)

