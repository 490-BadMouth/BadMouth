import socket
import pyaudio

CORAL_IP = "192.168.100.2"  # Replace with the Google Coral's static IP address
PORT = 5000
CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

def main():
    # Initialize the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((CORAL_IP, PORT))

    print("Waiting for connection...")

    # Receive the connection request from the host
    while True:
        data, host_addr = sock.recvfrom(CHUNK)
        if data == b"connect":
            sock.sendto(b"connected", host_addr)
            break

    print("Connected to host @: ", host_addr)

    # Initialize the PyAudio object
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("Sending audio stream to", host_addr)
    try:
        while True:
            data = stream.read(CHUNK)
            
            sock.sendto(data, host_addr)
    except Exception as e:
        print("Error while streaming audio:", e)
    except KeyboardInterrupt:
        print("Keyboard interrupt!!!")
        stream.stop_stream()
        stream.close()
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
        sock.close()

if __name__ == "__main__":
    main()
