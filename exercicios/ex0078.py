valores = list()
for n in range(0,5):
	valores.append(int(input(f'Digite um valor para a posição {n}: ')))
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitdo foi {max(valores)} nas posições ', end='')
for i, v in enumerate(valores):
	if v == max(valores):
		print(f'{i}...', end=' ')
print() 
print(f'O menor valor digitado foi {min(valores)} nas posições ', end='')
for i, v in enumerate(valores):
	if v == min(valores):
		print(f'{i}...', end=' ')
print()