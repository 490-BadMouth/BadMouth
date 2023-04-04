
# audio_sender.py
import socket
import pyaudio

CORAL_IP = "192.168.100.2"  # Replace with the Google Coral's static IP address
PORT = 5000
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

def main():
    # Initialize the socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((CORAL_IP, PORT))

        print("Waiting for connection...")

        # Receive the connection request from the host
        data, host_addr = sock.recvfrom(CHUNK)

        # Initialize the PyAudio object
        p = pyaudio.PyAudio()
        try:
            stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
            try:
                print("Sending audio stream to", host_addr)

                while True:
                    data = stream.read(CHUNK)
                    sock.sendto(data, host_addr)
            except Exception as e:
                print("Error while streaming audio:", e)
            finally:
                stream.stop_stream()
                stream.close()
        finally:
            p.terminate()

if __name__ == "__main__":
    main()

