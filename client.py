import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    send = b'''{"user":"Admin","password":"password123"}'''
    
    s.sendall(send)

    data = s.recv(1024)
print(send.decode())
print(f"Received {data.decode()}")

input()
