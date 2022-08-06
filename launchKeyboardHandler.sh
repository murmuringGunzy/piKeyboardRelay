cd /home/pi/Desktop
lxterminal -e python keyboardListener.py &
lxterminal -e sudo python comHandler.py &
matchbox-keyboard &