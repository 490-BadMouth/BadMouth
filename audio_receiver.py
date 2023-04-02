import socket
import os

# Configuration
CHUNK = 1024 * 4
FORMAT = "s16le"  # Little-endian 16-bit signed integer format
CHANNELS = 1
RATE = 44100
LISTEN_PORT = 5000
PIPE_PATH = "/tmp/Badmouth"

# Set up UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", LISTEN_PORT))

# Open the named pipe for writing
with open(PIPE_PATH, "wb") as pipe:
    print("Receiving audio...")

    while True:
        data, _ = sock.recvfrom(CHUNK * CHANNELS * 4)
        pipe.write(data)
        
