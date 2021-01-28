from random import randint
cont = 0
val_computador = randint(0,10)
print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPÁR')
print('=-' * 15)
while True:
	val_jogador = int(input('Digite um valor: '))
	soma = val_computador + val_jogador
	jogada = str(input('Para ou Ímpar? [P/I] ')).strip().upper()[0]
	if jogada == 'P':
		jogada = 'PAR'
	elif jogada == 'I':
		jogada = 'ÍMPAR'
	if soma % 2 == 0:
		resultado = str('PAR')
	else:
		resultado = str('ÍMPAR')
	print('-' * 30)
	print(f'Você jogou {val_jogador} e o computador {val_computador}. Total de {soma} DEU {resultado}')
	print('-' * 30)
	if jogada == resultado:
		print('Você VENCEU!')
		print('Vamos jogar novamente...')
		print('=-' * 17)
		cont += 1
	else:
		print('Você PERDEU!')
		print('=-' * 17)
		break
print(f'GAME OVER! Você venceu {cont} vez(es).')
