import serial
import time

def main():
        print('comHandler is listening and waiting for matlab...')
        ser = serial.Serial('/dev/serial0',115200) # serial object
        # main loop
        while 1:
                data = b''
                # wait for anything to come over serial
                while data == b'':
                        data = ser.readline()
                        time.sleep(1)
                # check if the word is 'start'
                data = data[0:-1].decode() # leaves off '\n'
                if data == 'start':
                        print('Sending the last line of keyOut.txt back to matlab')
                        insert_NL()
                        ser.write(get_last_line().encode())
                else:
                        print("MATLAB sent '{}', send 'start' to get data back".format(data))


def get_last_line():
        with open('keyOut.txt') as f:
                for line in f:
                        pass
                return line

def insert_NL():
        with open('keyOut.txt','a') as f:
                f.write('\n')

if __name__ == '__main__':
        main()
