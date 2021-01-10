from random import randint
from time import sleep
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
computador = randint(0,2)
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1.0)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 20)
print('Computador jogou {}'.format(computador))
print('Jogador jogou {}'.format(jogador))
print('-=' * 20)
if jogador == computador:
	print('EMPATE')
elif jogador == 0:
	if computador == 1:
		print('COMPUTADOR VENCE')
	elif computador == 2:
		print('JOGADOR VENCE')
elif jogador == 1:
	if computador == 0:
		print('JOGADOR VENCE')
	elif computador == 2:
		print('COMPUTADOR VENCE')
elif jogador == 2:
	if computador == 0:
		print('COMPUTADOR VENCE')
	elif computador == 1:
		print('JOGADOR VENCE')
