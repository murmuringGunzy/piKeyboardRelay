The files in this directory are written by Jaydon Gunzburg
to communicate back to MATLAB what has been typed into the
virtual keyboard, since the last time it asked.
run 'sh launchKeybourdListener.sh' to setup environment.

keyboardListener.py - run in background and constantly logs
any keystrokes to the file keyOut.txt.

comHandeler - constantly listens to serial port (connected
to matlab machine) for the work 'start'. When it receives
this word, it will add a new line to keyOut.txt, then send
the last line of that file back over serial.
MATLAB is expected to send 'start', wait, then read then
read what is send back straight away.

launchKeyboardListener.sh - simple shell script to run
afformentioned files in their own terminal windows, and
launch the virtual keyboard.