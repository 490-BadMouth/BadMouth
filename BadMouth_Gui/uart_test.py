from periphery import Serial

uart1 = Serial("/dev/ttyS1", 9600)

try:
    while True:
        #uart1.write(b"Testing")
        buf = uart1.read(128, 0.5)
        #print("read {:d} bytes: _{:s}_".format(len(buf), buf))
        print(buf)
except KeyboardInterrupt:
    uart1.close()
    print("Serial Closed")