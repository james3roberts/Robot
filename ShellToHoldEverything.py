##File to contain everything for the robot.
## SensorAsPartOFWhole is for the motor.
##distance1 is to get the distance1
##distance2 is to measure the motor
## button is to get the distance1 and send to distance2
import SensorAsPartOFWhole.py
import distance1.py


#going to try and get the motor to move the tape 6 inches.
execfile('distance1.py')
if distance in distance1 != 6:
    execfile('SensorAsPartOFWhole.py')
     