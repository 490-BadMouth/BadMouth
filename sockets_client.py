import socket

HOST = '192.168.100.57'  # localhost
PORT = 5000        # same arbitrary port number as server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall('Hello, World!'.encode())
    data = s.recv(1024)
    print(f'Received: {data.decode()}')