from math import factorial
n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
# Usando o while praticamente um substituto do for
print('Calculando {}! = '.format(n), end='')
while c > 0:
	print('{}'.format(c), end='')
	print(' x ' if c > 1 else ' = ', end='') #if dentro de um print
	c -= 1
c = factorial(n)
print('{}'.format(c))
# print('O fatorial de {} é {}'.format(n, c))