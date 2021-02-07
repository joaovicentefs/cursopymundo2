valores = list()
while True:
	item = int(input('Digite um valor: '))
	if item not in valores:
		valores.append(item)
		print('Valor adicionado com sucesso...')
	else:
		print('Valor duplicado! Não vou adicionar...')
	resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
	if resp == 'N':
		break
print('-=' * 30)
valores.sort()
print(f'Você digitou os valores ', end='')
for n in valores:
	print(f'{n}', end=' ')
print('\n')		
