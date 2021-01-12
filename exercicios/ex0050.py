soma = 0
cont = 0
for c in range(1,7):
	n = int(input('Digite o {}° número inteiro: '.format(c)))
	if n % 2 == 0:
		soma += n
		cont += 1
print('Somando apenas os {} números pares digitados o resultado é {}'.format(cont, soma))
