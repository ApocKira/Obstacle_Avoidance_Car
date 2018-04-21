#! /usr/bin/python3
import RPi.GPIO as GPIO
import sys
import time
import Ultrasonic_Module as Ul
import Motor_Module as Mo


ultrasonic=Ul.Ultrasonic_Module(25,26)
motor=Mo.Motor_Module()
print("#########initing the ultrasonic module...##########")
if not ultrasonic.setup():
    print("ultrasonic setup fall , programe stop")
    exit()
print("#########initing the motor module...##########")
motor.setup()


print("the car start running...") 
motor.ahead()


distance=10
limited_d=0.05 
time_rear=0.8  
time_right=1.2  
try:
   while True:
      distance=ultrasonic.getdistance()
      if distance <= limited_d:
          print("run into blank wall")
          motor.stop()
          motor.rear(time_rear)
          motor.right(time_right)
          motor.ahead()
except KeyboardInterrupt:
    motor.stop()
    print("")
    print("stop the car")