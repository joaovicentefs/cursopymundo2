from random import randint
from time import sleep
cont = 0
numero = randint(0, 10)
print('-=' * 22)
print('Eu vou pensar em número entre 0 e 10. Você consegue adivinhar?')
print('-=' * 22)
chute = int(input('Tente advinhar, qual número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
while chute != numero:
	chute = int(input('Você errou! Tente novamente: '))
	cont += 1
	if chute > 
if cont == 1:
	print('CORRETO! O Computador pensou em {}! E você acertou de primeira!'.format(numero))
elif cont > 1:
	print('CORRETO! O Computador pensou em {}! E você precisou de {} chutes para acertar!'.format(numero, cont))
