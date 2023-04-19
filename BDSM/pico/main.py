# Python program for the Pico slave mode
import machine
from machine import Pin
import utime

#led = Pin(25, Pin.OUT)
#Rx_Pin = 2  # UART0 of the pico Rx
#Tx_Pin = 3  # UART0 of the pico Tx
#uart = machine.UART(1, baudrate=115200, tx=machine.Pin(Tx_Pin), rx=machine.Pin(Rx_Pin))
# Creates uart object ^

# Loop to receive and send data over UART
#while True:
#    if uart.any():
#        led.value(1)
#        data = uart.read(10)
#        print("Received Mini: ", data)
#        # Send message back
#        uart.write("Hello from Pico".encode())
#        led.value(0)  # Turn off the LED after sending data
#    utime.sleep_ms(100)

Rx_Pin = 2  # UART0 of the Pico Rx
Tx_Pin = 3  # UART0 of the Pico Tx
uart = machine.UART(1, baudrate=115200, tx=machine.Pin(Tx_Pin), rx=machine.Pin(Rx_Pin))

while True:
    if uart.any():
        data = uart.read(10)
        print("Received from Coral Mini: ", data)
        uart.write(b'ACK')  # Send "ACK" back to the Coral Mini
    utime.sleep_ms(100)


