from random import randint
from time import sleep
partida = {'jogador1': randint(1, 6),
			'jogador2': randint(1, 6),
			'jogador3': randint(1, 6),
			'jogador4': randint(1, 6)}
print('Valores Sorteados:')
for k, v in partida.items():
	print(f'{k} tirou {v}')
	sleep(0.5)