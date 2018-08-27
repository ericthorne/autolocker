# autolocker

This is the source code to an Raspberry Pi Zero W project that controls car remote key fobs.

There are multiple ways to refer to Raspberry Pi pins, this webpage as a good table at the
end showing them:
https://learn.sparkfun.com/tutorials/raspberry-gpio/gpio-pinout

# toggle_4_5.sh
The main script is toggle_4_5.sh which toggles WiringPi defined pin numbers 4 and 5 when run
from 0->1.  These pins are connected to the outputs of the buttons via header wires soldered to
the buttons.

# int_gpio.py
I wanted a way to run toggle_4_5.sh with a virtual push button (in my case, I remove and re-insert
a wire connected from GPIO14 to GPIO25 on the GPIO14 side).

# crontab__root.txt
The crontab listing to start things up correctly and run toggle_4_5.sh at 11PM each night.  Needs
to be run as root, so use `sudo crontab -e`.

# BOM:
1 Raspberry Pi Zero W kit: https://www.amazon.com/CanaKit-Raspberry-Wireless-Complete-Starter/dp/B072N3X39J
3 wires from: https://www.amazon.com/gp/product/B01MU0IMFF/
(cut in half)
1 key fob for a 2000 Toyota:https://www.amazon.com/gp/product/B06XRGQ3LJ/
1 key for a 2009 Toyota: https://www.amazon.com/gp/product/B06Y2F1HS4/
(I was paranoid I'd destroy a remote so I ordered 2 packs)
