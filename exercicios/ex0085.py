numeros = [[], []]
for c in range(1, 8):
	valor = int(input(f'Digite o {c}º valor: '))
	if valor % 2 == 0:
		numeros[0].append(valor)
	elif valor % 2 == 1:
		numeros[1].append(valor)
print('-=' * 30)
numeros[0].sort()
print(f'Os valores pares digitados foram: {numeros[0]}')
numeros[1].sort()
print(f'Os valores ímpares digitados foram: {numeros[1]}')
