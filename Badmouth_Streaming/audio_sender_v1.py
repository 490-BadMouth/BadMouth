
import pyaudio
import socket
import struct

# Configuration
CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100  # CD quality audio
DEST_IP = "HOST_IP"  # Replace with the IP address of your desktop computer
DEST_PORT = 5000

# Set up PyAudio
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

# Set up UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Streaming audio...")

while True:
    data = stream.read(CHUNK, exception_on_overflow=False)
    sock.sendto(data, (DEST_IP, DEST_PORT))
