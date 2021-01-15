inv = ''
frase = str(input('Digite uma frase: ')).strip().lower()
semespaco = frase.replace(' ', '')
tot = int(len(semespaco))
for c in range(tot - 1, -1, -1):
	inv += str(semespaco[c])
print('O inverso de {} é {}'.format(semespaco, inv))
if semespaco == inv:
	print('Temos um Palíndromo')
else:
	print('A frase digitada não é um Palíndromo')