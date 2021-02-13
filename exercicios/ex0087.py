matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = soma3 =  maiorl2 = 0
for l in range(0, 3):
	for c in range(0, 3):
		matriz[l][c] = int(input(f'Digite um valor para [{l + 1}, {c + 1}]: '))
		if matriz[l][c] % 2 == 0:
			somap += matriz[l][c]
		if c == 2:
			soma3 += matriz[l][c]
		if len(matriz) == 1 and c == 0:
			maiorl2 = matriz[l][c]
for c in matriz[1]:
	if c == matriz[1][0]:
		maiorl2 = c
	else:
		if c > maiorl2:
			maiorl2 = c
print('-=' *30)
for l in range(0, 3):
	for c in range(0, 3):
		print(f'[{matriz[l][c]:^5}]', end='')
	print()
print('-=' * 30)
print(f'A soma dos valores pares é {somap}.')
print(f'A soma dos valores da terceira coluna é {soma3}.')
print(f'O maior valor da segunda linha é {maiorl2}.')

