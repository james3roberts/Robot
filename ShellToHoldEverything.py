##File to contain everything for the robot.
## SensorAsPartOFWhole is for the motor.
##distance1 is to get the distance the motor moves
##distance2 is to measure how far the motor should ove. 
## button will be used as a way to mark measurements. 

#OK i think defining a function to call distance1 and then and if statement to run the motor.
#if that does not work then might have to wright the two together. or call them at the smae time


# I think i found a simpler way and there is still errors that I dont know how to fix

# first try. hope this goes somewhere. 
# information about def a function from w3school.com

# import time

# #import SensorAsPartOFWhole

# #this function should get the distance from distance1 and print the value
# def d1(mdistance):
#     import distance1
#     value = distance1.get_value(distance)
#     print(value)

# #this should turn on the motor.
# def m1 (motor):
#     import SensorAsPartOFWhole


# if d1 != 6:
#     m1
# if d1 == 6:
#     exit

#the exit at the bottom should kill the program
#This might need to be put in a loop 
import time

import distance1
from distance1 import distance
if distance != 6:
    import SensorAsPartOFWhole
else:
    exit()





