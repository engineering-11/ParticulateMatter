##particulate matter take off code
import serial
import time
ser = serial.Serial('/dev/ttyUSB0')
x=0
while x < 1:
    data = ser.read(32)
    extract =(data[5]<<8)+data[6]
    print("PM 2.5 Concentration is",extract,"ug/m^3")
    time.sleep(5)



