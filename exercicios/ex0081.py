lista = list()
cont = 0
while True:
	lista.append(int(input('Digite um valor: ')))
	cont += 1
	resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
	if resp == 'N':
		break
print('-=' * 30)
print(f' Você digitou {cont} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
for n in lista:
	if n == 5:
		cinco = True
	else:
		cinco = False
if cinco == True:		
	print('O valor 5 faz parte da lista.')
else:
	print('O valor 5 não foi encontrado na lista')
