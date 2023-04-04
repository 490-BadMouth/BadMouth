
# audio_receiver.py
import socket

CORAL_IP = "192.168.100.2"  # Replace with the Google Coral's static IP address
PORT = 5000
CHUNK = 1024 * 4
PIPE_PATH = "/tmp/Badmouth"

def main():
    # Initialize the socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:

        # Send a connection request to the Coral
        sock.sendto(b"connect", (CORAL_IP, PORT))

        print("Receiving audio stream...")

        try:
            with open(PIPE_PATH, "wb") as pipe:
                while True:
                    data, _ = sock.recvfrom(CHUNK * 4)
                    pipe.write(data)
        except Exception as e:
            print("Error while receiving audio stream:", e)
            socket.close()

if __name__ == "__main__":
    main()

