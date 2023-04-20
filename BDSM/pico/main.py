# Python program for the Pico slave mode
import machine
from machine import Pin
import time

led = Pin(25, Pin.OUT)
RX_PIN = 2   # Pin 2 for RX on Pico
TX_PIN = 3   # Pin 3 for TX on Pico


# Create a UART object
uart = machine.UART(1, baudrate=115200, tx=machine.Pin(TX_PIN), rx=machine.Pin(RX_PIN))

while True:
    if uart.any():
        led.value(1)
        data = uart.read(10)
        print("Received data:", data)
        # Send a response back
        uart.write("Hello from Pico!".encode())
    time.sleep(0.5)  # Add a delay between each send-receive cycle



