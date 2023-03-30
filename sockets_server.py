import socket

HOST = '192.168.100.57'  # localhost
PORT = 5000        # arbitrary port number

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Server listening on {HOST}:{PORT}')
    conn, addr = s.accept()
    with conn:
        print(f'Connected by {addr}')
        data = conn.recv(1024)
        if data:
            print(f'Received: {data.decode()}')
            conn.sendall('Hello, World!'.encode())
