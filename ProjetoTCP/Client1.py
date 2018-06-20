import socket

h = input("Digite o IP: ")
p = int(input("Digite a Porta: "))


j1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

j1.connect((h, p))

while True:
    j1.recvfrom(1024)
    msg = input()
    j1.send (msg.encode())

j1.close()
