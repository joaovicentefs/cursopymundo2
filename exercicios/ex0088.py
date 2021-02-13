from random import randint
from time import sleep
palpites = list()
jogo = list()
print('-' * 40)
print('{:^40}'.format("JOGA NA MEGA SENA"))
print('-' * 40)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(1, qtd + 1):
	for c in range(0, 6):
		jogo.append(randint(1, 60))
	palpites.append(jogo[:])
	jogo.clear()
print('-=' * 3,f'SORTEANDO {qtd} JOGOS', '-=' * 3)
for j in range(1, qtd +1):
	palpites[j -1].sort()
	print(f'Jogo {j}: {palpites[j - 1]}')
	sleep(0.5)
print('-=' * 5,' < BOA SORTE > ', '-=' * 5)
# MEU PROGRAMA FUNCIONA
# Preciso fazer a melhoria nele para que ele não permita repetição de número dentro da lista
# Ver a solução do Guanarabara para isso