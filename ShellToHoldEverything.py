##File to contain everything for the robot.
## SensorAsPartOFWhole is for the motor.
##distance1 is to get the distance the motor moves
##distance2 is to measure how far the motor should ove.
## button will be used as a way to mark measurements.



# this should get the sensor to run and stop at 6cm
#I added the while statement to see if this will get it to keep running
# added the print statement to get the distance. 
# dont know what will work and cant check itto

import time

from distance1 import distance
while distance <=6:
    print(distance)
    import SensorAsPartOFWhole
else:
    exit()

#if this works then we need to add another sensor and a button.
