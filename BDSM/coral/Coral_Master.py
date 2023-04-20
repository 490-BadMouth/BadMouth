# Coral Mini Master Code
import machine
import time
import serial

Rx_Pin = 10  # UART0 RX pin on the Coral Mini
Tx_Pin = 8  # UART0 TX pin on the Coral Mini

ser = serial.Serial('/dev/ttyGS0', 115200)  # Set the timeout to 1 second

while True:
    ser.write('Hello from the Coral Mini'.encode())  # Send data over UART0
    time.sleep(0.5)  # Add a short delay before reading the response
    data = ser.read(10)  # Read data from UART0 of the Pico
    if data:
        print("Pico Received: ", data)
        ser.write('Hello from Coral Mini!'.encode()) # Send a response back to the Pico
    time.sleep(0.5)  # Add a delay between each send-receive cycle

