from random import randint
from time import sleep
palpites = list()
jogo = list()
print('-' * 40)
print('{:^40}'.format("JOGA NA MEGA SENA"))
print('-' * 40)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= qtd:
	cont = 0
	while True:
		num = randint(1, 60)
		if num not in jogo:
			jogo.append(num)
			cont += 1
		if cont >= 6:
			break
	jogo.sort()	
	palpites.append(jogo[:])
	jogo.clear()
	tot += 1
print('-=' * 3,f'SORTEANDO {qtd} JOGOS', '-=' * 3)
for j in range(1, qtd +1):
	palpites[j -1].sort()
	print(f'Jogo {j}: {palpites[j - 1]}')
	sleep(1)
print('-=' * 5,' < BOA SORTE > ', '-=' * 5)
