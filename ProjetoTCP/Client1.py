import socket

host = "127.0.0.1"
port = 7205

j1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

j1.connect((host, port))

while True:
    j1.recvfrom(bufsize)
    msg = input()
    j1.send (msg.encode())
    j1.recvfrom(bufsize)

j1.close()
