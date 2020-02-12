##This is to get the distance1 sensor to get lengths.
## Code is from DistanceSensor on the pi. 

#going to try to make this a function
#I think I know how to call a function in a different script

def get_distance():
    import RPi.GPIO as GPIO
    import time
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
            
        finally:
            GPIO.cleanup()


#All i added what the info on line 7 and tried to turn it into a function.
# then i added a tab to every line to fix just delete line 7
# #and untab every line 
# 
# I might of needed to creat the motor file into a function.  