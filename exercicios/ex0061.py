primeiro = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
decimo = primeiro + (10 - 1) * raz
c = primeiro
# print('O Décimo termo de uma PA, inciado em {} e com razão de {} é {}'.format(primeiro, raz, decimo))
while c < decimo + raz:
	print('{}'.format(c), end=' --> ')
	c += raz
print('FIM!')
