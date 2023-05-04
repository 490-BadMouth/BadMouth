import serial
import time

# Set up a virtual UART connection through the USB-C port
ser = serial.Serial('/dev/ttyGS0', 115200, timeout=1)

while True:
    # Send data over UART
    ser.write(b'Hello from Coral Mini')
    time.sleep(1)
