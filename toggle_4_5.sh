#!/bin/sh

# Turn io's to outputs
gpio mode 4 out
gpio mode 5 out

# Turn output on
gpio write 4 0
gpio write 5 0

# how long is a typical button press?
sleep 0.5

# Turn output off
gpio write 4 1
gpio write 5 1
