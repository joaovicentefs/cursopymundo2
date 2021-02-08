lista = list()
cont = 0
while True:
	lista.append(int(input('Digite um valor: ')))
	cont += 1
	resp = str(input(' Deseja continuar? [S/N] ')).strip().upper()[0]
	if resp == 'N':
		break
print(f' Você digitou {cont} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
