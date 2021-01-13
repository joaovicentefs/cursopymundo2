cont = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
	divi = num % c
	if divi == 0:
		cont += 1
print('O número {} foi divísivel {} vezes'.format(num, cont))
if cont == 2:
	print('E por isso ele É PRIMO')
else:
	print('E por isso ele NÃO É PRIMO')
