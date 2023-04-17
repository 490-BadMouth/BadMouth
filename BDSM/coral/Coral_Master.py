#Coral Mini Master Code
import serial
Rx_Pin = 10; #UART0 RX pin on the coral mini
Tx_Pin = 8; #UART0 TX pin on the coral mini

ser = serial.Serial('/dev/ttyS0',115200,timeout=0);#open serial communication at baud rate of 115200
ser.write('Hello from the Coral Mini'.encode());#send data over UART0
data = ser.read(10);#Read data from UART0 of the Pico
print("Pico Received: ", data);
ser.close()#close serial communication

