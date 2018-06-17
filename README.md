# rpi-temp-control

A temperature monitor and control program for the Raspberry Pi's CPU. This is done by monitoring the reported temperature
of the combined CPU and GPU package, which is fed into a PID loop that controls the speed of a fan mounted above it.

I wrote this so my Pi would be quite when it is doing simple tasks, but would be able to enable a fan to cool the CPU
when I need to compile things or surf the web.

# Using

To run this program, you are going to need root privileges but can be run by simply entering

```
# python rpi-temp-control.py
``` 

This will leave the program running forever, and you should notice the fan changing speed as the Pi gets warmer and
cooler. At some point I will turn this into a proper daemon service that can be setup and forgotten about.

There are only a couple of things that should be noted when using this, first that you need to connect a fan to the Pi
in a safe way. You should NOT drive the fan from the gpio pins on the Pi directly, but instead the pin that this
program controls should be some sort of enable line on either a power transistor or motor control board. The second
thing is that this program is writing a pwm signal to that pin, which means the fan is really turning on and off quickly
and may make not allow this program to work with motor controllers that use other methods to control motor speed. Also
be aware that there is probably a minimum speed (or pulse rate) that the fan will work at, so the minimum fan speed
may need to be tweaked because of that.

Please don't expect this to solve all overheating issues your Pi may experience, this just a dumb PID loop. Really any
Raspberry Pi 3 (at least in my experience) should have at least a heatsink on their CPU to help with limiting when
thermal throttling will happen. A case or mounting for a fan should have enough airflow for the fan so it won't burn out
the motor, but if the air the fan is moving across the CPU will limit how cool it can make the CPU.
# Copyright and License

2018 Matt Kohls
GPL v3

Based on the work by [rudybrian](https://github.com/rudybrian/PID_Fan_Control)

This program is distributed in the hope it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.