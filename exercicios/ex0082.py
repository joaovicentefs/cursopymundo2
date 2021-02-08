lista = list()
pares = list()
impares = list()
while True:
	lista.append(int(input('Digite um número: ')))
	resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
	if resp == 'N':
		break
for n in lista:
	if n % 2 == 0:
		pares.append(n)
	elif n % 2 == 1:
		impares.append(n)
print('-=' * 30)		
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
