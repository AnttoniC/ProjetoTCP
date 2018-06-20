import socket
import sys
import os

h = "0.0.0.0"
p = 7205
j = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
jtest = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
jogadat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = "X"
o = "O"
tamanho = 0
err = 2
jog = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((h, p))
s.listen(2)

print("Ouvindo rede ", h, p)
print("esperando conexão")
(obj, ip) = s.accept()
print(ip[0], " Conectado")


def Jinvalida(err):
    if (err == 0):
        print("-----------------------Jogada invalida Do Jogador 1------------------------------")
        obj.send(b"-----------------------Jogada invalida Do Jogador 1-----------------------\n")
    elif (err == 1):
        print("-----------------------Jogada invalida Do Jogador 2------------------------------")
        obj.send(b"-----------------------Jogada invalida Do Jogador 2-----------------------\n")

def XouO(vetor):
	if (vetor == "X"):
		return "X"
	else:
		return "O"

def jv():
	# verifica se o jogador ganhou na orizontal
	if (j[0][0] == j[0][1] and j[0][0] == j[0][2] and j[0][0] != " " and j[0][1] != " " and j[0][2] != " "):
		return XouO(j[0][0])
	elif (j[1][0] == j[1][1] and j[1][0] == j[1][2] and j[1][0] != " " and j[1][1] != " " and j[1][0] != " "):
		return XouO(j[1][0])
	elif (j[2][0] == j[2][1] and j[2][0] == j[2][2] and j[2][0] != " " and j[2][1] != " " and j[2][0] != " "):
		return XouO(j[2][0])
	# verifica se o jogador ganhou na vertical
	elif (j[0][0] == j[1][0] and j[0][0] == j[2][0] and j[0][0] != " " and j[1][0] != " " and j[2][0] != " "):
		return XouO(j[0][0])
	elif (j[0][1] == j[1][1] and j[0][1] == j[2][1] and j[0][1] != " " and j[1][1] != " " and j[2][1] != " "):
		return XouO(j[1][1])
	elif (j[0][2] == j[1][2] and j[0][2] == j[2][2] and j[0][2] != " " and j[1][2] != " " and j[2][2] != " "):
		return XouO(j[2][2])
	# verifica se o jogador ganhou cruzado
	elif (j[0][0] == j[1][1] and j[0][0] == j[2][2] and j[0][0] != " " and j[1][1] != " " and j[2][2] != " "):
		return XouO(j[2][2])
	elif (j[0][2] == j[1][1] and j[0][2] == j[2][0] and j[0][2] != " " and j[1][1] != " " and j[2][0] != " "):
		return XouO(j[1][1])
	# verifica empate
	else:
		if (jog == 9):
			return 9

def jogada(jo, escolha):
    for i1 in range(3):
        for i2 in range(3):
            if (jtest[i1][i2] == jo):
                if (j[i1][i2] != " "):
                    Jinvalida(err)
                else:
                    j[i1][i2] = escolha
                    jogadat[i1][i2] = " "


def tela1():
    limpar = os.system('cls' if os.name == 'nt' else 'clear')
    # tela jogador1
    sep = "|---+---+---|		|---+---+---|\n"
    obj.send(b"|============================================|\n")
    m = "| %s | %s | %s |		| %s | %s | %s |\n" % (
    j[0][0], j[0][1], j[0][2], jogadat[0][0], jogadat[0][1], jogadat[0][2])
    obj.send(m.encode())
    obj.send(sep.encode())
    m = "| %s | %s | %s |		| %s | %s | %s |\n" % (
    j[1][0], j[1][1], j[1][2], jogadat[1][0], jogadat[1][1], jogadat[1][2])
    obj.send(m.encode())
    obj.send(sep.encode())
    m = "| %s | %s | %s |		| %s | %s | %s |\n" % (
    j[2][0], j[2][1], j[2][2], jogadat[2][0], jogadat[2][1], jogadat[2][2])
    obj.send(m.encode())
    obj.send(b"|============================================|\n")
def tela2():
    # tela jogador 2
    sep = "|---+---+---|		|---+---+---|\n"
    print("|============================================|\n")
    print("| %s | %s | %s |		| %s | %s | %s |\n" % (
    j[0][0], j[0][1], j[0][2], jogadat[0][0], jogadat[0][1], jogadat[0][2]))
    print(sep)
    print("| %s | %s | %s |		| %s | %s | %s |\n" % (
    j[1][0], j[1][1], j[1][2], jogadat[1][0], jogadat[1][1], jogadat[1][2]))
    print(sep)
    print("| %s | %s | %s |		| %s | %s | %s |\n" % (
    j[2][0], j[2][1], j[2][2], jogadat[2][0], jogadat[2][1], jogadat[2][2]))
    print("|============================================|\n")


print()

tela1()
tela2()
while True:
	try:
		#Jogador 1
		err = 0
		obj.send(b"Jogador1\n")
		obj.send(b"Tabla atualizada\n")
		obj.send(b"Sua vez de jogar\n")
		print("Vez do jogador 1")
		vez = obj.recv(1024)
		vez = int(vez)
		if (vez > 9):
			Jinvalida(err)
			obj.send(b"Observe o mapa a sua direita e tente novamente: \n")
			print("Observe o mapa a sua direita e tente novamente: ")
		else:
			jogada(vez,x)
		tela1()
		tela2()
		jog = jog + 1
		if (jv() == "X"):
			obj.send(b"---------------------Jogador 1 Ganhou\n")
			print("---------------------Jogador 1 Ganhou\n")
			break
		elif (jv() == 9):
			obj.send(b"---------------------EMPATE\n")
			print("---------------------EMPATE\n")
			break
		# Jogador 2
		err = 1
		print("Jogador2\n")
		print("Tabela atualizada\n")
		print("Sua vez jogar\n")
		obj.send(b'vez do jogar 2\n')
		vez2 = int(input(""))
		jogada(vez2, o)
		jog = jog + 1
		tela1()
		tela2()
		if (jv() == "O"):
			obj.send(b"---------------------Jogador 2 Ganhou\n")
			print("---------------------Jogador 2 Ganhou\n")
			break
		elif (jv() == 9):
			obj.send(b"---------------------EMPATE\n")
			print("---------------------EMPATE\n")
			break
	except ValueError:
		Jinvalida(err)

s.close()
