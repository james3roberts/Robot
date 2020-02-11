#This code is emailed from the raspberry pi
#it works on the pi. 


import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
StepPins = [17,18,27,22]

for pin in StepPins:
  print ("Setup pins")
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]


StepCount = len(Seq)

StepDir = 2 # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise

 
if len(sys.argv)>1:
  WaitTime = int(sys.argv[1])/float(1000)
 
  
else:
  WaitTime = 10/float(1000)

StepCounter = 0

while True:

  print (StepCounter,)
  print (Seq[StepCounter])

  for pin in range(0, 4):
    xpin = StepPins[pin]
    if Seq[StepCounter][pin]!=0:
      print (" Enable GPIO %i" %(xpin))
      GPIO.output(xpin, True)
    else:
      GPIO.output(xpin, False)

  StepCounter += StepDir


  if (StepCounter>=StepCount):
    StepCounter = 0
  if (StepCounter<0):
    StepCounter = StepCount+StepDir

  time.sleep(WaitTime)
print(StepCounter)
#This does not pring on linux or idle. Figure this out so you can get a total distance
print('I have no control over this')
print('I dont even understand how this works')
print('Finally figured something out')