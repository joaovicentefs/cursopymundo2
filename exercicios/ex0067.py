while True:
	num = int(input('Quer ver a tabuada de que número? '))
	if num < 0:
		break
	print('-' * 30)
	for c in range(1,11):
		print(f'{num} X {c} = {num * c}')
	print('-' * 30)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')
