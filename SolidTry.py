#maybe the proble is that I keep trying to make things to complicated
#what if I just make 1 big program and call it a day.
#as i start this it is 11pm and I cant sleep
#too much stress and a feeling of needing to get a win no matter how small
#might just be to much star wars comming out


#the goal of this program is to combine what I already have connected to the pi
#that is just the motor and the sensor. 
#once this works I will add more to the pi and then add more code. 


import RPi.GPIO as GPIO
import time
import sys

i = '0'
while i:
    try:
        GPIO.setmode(GPIO.BOARD)
        PIN_TRIGGER = 33
        PIN_ECHO = 37

        GPIO.setup(PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)

        GPIO.setup(PIN_TRIGGER, GPIO.LOW)
        print('wAITING FOR SENSOR TO SETTLE')
        time.sleep(2)
        print('Calculating the distance')
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(.01)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        
        while GPIO.input (PIN_ECHO)==0:
            pulse_start_time = time.time()
        while GPIO.input (PIN_ECHO)==1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance= round(pulse_duration * 17150 /2)
        print('Distance: ', distance, "cm")
        distanceIn = (distance / 2.54)
        print('Distance: ',distanceIn, "Inches")
        if distance <=10:
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
        get_value = distance



    finally:
        GPIO.cleanup()
