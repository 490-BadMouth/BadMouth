import serial
import time

ser = serial.Serial('/dev/ttyS0', 115200, timeout=1)

while True:
    ser.write(b'TEST')  # Send "TEST" to the Pico over UART
    time.sleep(0.5)  # Wait before reading the response
    data = ser.read(10)  # Read data from UART of the Pico
    if data:
        print("Received from Pico: ", data)
    time.sleep(1)
