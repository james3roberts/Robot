##This is to get the distance1 sensor to get lengths.

import RPi.GPIO as GPIO
import time
i = '0'
while i:
    try:
        GPIO.setmode(GPIO.BOARD)
        PIN_TRIGGER = 33
        PIN_ECHO = 37
        GPIO.setup(PIN_TRIGGER, GPIO.LOW)
        PRINT('wAITING FOR SENSOR TO SETTLE')
        time.sleep(2)
        print('Calculating the distance')
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(.01)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        
        while GPIO.input (PIN_ECHO)==0:
            pulse_start_time = time.time()
         while GPIO.input (PIN_ECHO)==1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_tiem - pulse_start_time
        distance= round(pulse_duration * 17150 /2)
        print('Distance: ', distance, "cm")
        distanceIn = (distance / 2.54)
        print('Distance: ',distanceIn, "Inches")
    finally:
        GPIO.cleanup()