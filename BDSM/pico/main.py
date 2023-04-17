#python program for the pico slave mode
import machine
import utime
Rx_Pin = 2 #UART0 of the pico Rx
Tx_Pin = 3 #UART0 pf the pico Tx
uart = machine.UART(1, baudrate = 115200, tx = machine.Pin(Tx_Pin), rx = machine.Pin(Rx_Pin))
#creates uart object ^
#loop to recieve and send data over UART
while True:
    if uart.any():
        data = uart.read(10)
        print("Received Mini: ", data)
        #send message back
        wait.write("Hello from Pico".encode())
    utime.sleep_ms(100)
