# autolocker

This is the source code to an Raspberry Pi Zero W project that controls car remote key fobs.

There are multiple ways to refer to Raspberry Pi pins, this webpage as a good table at the
end showing them:
https://learn.sparkfun.com/tutorials/raspberry-gpio/gpio-pinout

# toggle_4_5.sh
The main script is toggle_4_5.sh which toggles WiringPi defined pin numberss 4 and 5 when run i
from 0->1.  These pins are connected to the outputs of the buttons via header wires soldered to
the buttons.

# int_gpio.py
I wanted a way to run toggle_4_5.sh with a virtual push button (in my case, I remove and re-insert
a wire connected from GPIO14 to GPIO25).

# crontab__root.txt
The crontab listing to start things up correctly and run toggle_4_5.sh at 11PM each night.  Needs i
to be run as rootm so `sudo crontab -e`
