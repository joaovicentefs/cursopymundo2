soma = 0
for c in range(3, 501, 3):
	if c % 2 != 0:
		soma = soma + c
print('O resultado final de todos os números é de {}'.format(soma))
