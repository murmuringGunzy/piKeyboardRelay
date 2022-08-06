cd /home/pi/piKeyboardRelay
lxterminal -e python keyboardListener.py &
lxterminal -e sudo python comHandler.py &
#matchbox-keyboard &
