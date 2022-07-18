import serial
import time

# Open grbl serial port
s = serial.Serial('/dev/ttyACM0',115200)

# Open g-code file
f = "G91 X10 F1000"

# Wake up grbl
s.write(b'\r\n\r\n')
time.sleep(2)   # Wait for grbl to initialize 
s.flushInput()  # Flush startup text in serial input

# Stream g-code to grbl
for line in f:
    print('Sending: ' + f),
    mensagem=f+'\n'
    s.write(mensagem.encode()) # Send g-code block to grbl
    grbl_out = s.readline() # Wait for grbl response with carriage return
    print(' : ' + grbl_out.decode().strip())

# Wait here until grbl is finished to close serial port and file.
# raw_input("  Press <Enter> to exit and disable grbl.") 

# Close file and serial port

s.close()  

'''
## Alguns comandos do serialport ##
#ser.close()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lsusb to check device name
#dmesg | grep "tty" to find port name
import serial,time
if __name__ == '__main__':
    
    print('Running. Press CTRL-C to exit.')
    with serial.Serial("/dev/ttyACM0", 115200, timeout=1) as arduino:
        time.sleep(0.1) #wait for serial to open
        if arduino.isOpen():
            print("{} connected!".format(arduino.port))
            try:
                while True:
                    cmd=input("Enter command : ")
                    arduino.write(cmd.encode())
                    #time.sleep(0.1) #wait for arduino to answer
                    while arduino.inWaiting()==0: pass
                    if  arduino.inWaiting()>0: 
                        answer=arduino.readline()
                        print(answer)
                        arduino.flushInput() #remove data after reading
            except KeyboardInterrupt:
                print("KeyboardInterrupt has been caught.")
'''
                
'''
import serial
from serial.tools import list_ports
ser = serial.Serial('/dev/ttyACM0', 9600)
print(ser.name)

from time import sleep
#Serial takes these two parameters: serial device and baudrate
while True:
    received_data = ser.read()              #read serial port
    sleep(0.03)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    print (received_data)                   #print received data
    ser.write(received_data)                #transmit data serially 
print("Sai do while")
'''