# Coral Mini Master Code
import serial
import time

Rx_Pin = 10  # UART0 RX pin on the Coral Mini
Tx_Pin = 8  # UART0 TX pin on the Coral Mini

ser = serial.Serial('/dev/ttyS0', 115200, timeout=1)  # Set the timeout to 1 second

while True:
    ser.write('Hello from the Coral Mini'.encode())  # Send data over UART0
    time.sleep(0.5)  # Add a short delay before reading the response
    data = ser.read(10)  # Read data from UART0 of the Pico
    if data:
        print("Pico Received: ", data)
    time.sleep(1)  # Add a delay between each send-receive cycle
