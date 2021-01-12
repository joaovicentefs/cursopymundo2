soma = 0
for c in range(0,6):
	n = int(input('Digite um número inteiro: '))
	if n % 2 == 0:
		soma += n
print('Somando apenas os números pares digitados o resultado é {}'.format(soma))
