#!/usr/bin/env python3

##
# rpi-temp-control
#
#
#
# Matt Kohls

import subprocess
from gpiozero import Motor
from pid import PID
from time import sleep

# Defaults
TEMP_TARGET = float(47.0)
FAN_PIN = 17   # Pin the fan control is tied to
DUMMY_PIN = 18 # Any unused pin. Used to setup Motor from gpiozero
MIN_FAN_SPEED = 80 / 100

## Grabs Temperature of GPU/CPU
#
# @return temperature of GPU/CPU
def grab_temp():
    try:
        file = open("/sys/class/thermal/thermal_zone0/temp", "r")
        val = int(file.readline()) / 1000
        file.close()
        return val
    except:
        print("Error reading from thermal zone")
        return 0

# Initial loop setup
ploop = PID(1, 1, .02, Integrator_max=100, Integrator_min=0, Set_Point=TEMP_TARGET)
cycle = 1
fan = Motor(FAN_PIN, DUMMY_PIN)
fan.forward(cycle)
last_duty_cycle = 0
last_temp = 0

while True:
    sleep(1)
    temp = grab_temp()
    print(temp)
    cycle_change = (ploop.update(temp)) * -1
    cycle = (100 + int(cycle_change)) / 100 # Since fan.forward() wants a number between 0 and 1

    if cycle <= .2:
        cycle = 0
    elif cycle > 1:
        cycle = 1
    elif cycle < MIN_FAN_SPEED:
        cycle = MIN_FAN_SPEED

    if cycle == 0:
        fan.stop()
    elif last_duty_cycle != cycle:
        fan.forward(cycle)
    last_duty_cycle = cycle