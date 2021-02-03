from random import randint
maior = menor = cont = 0
sorteio = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('Os valores sorteados foram: ', end='')
maior = menor = 0
for num in sorteio:
	cont += 1
	if cont != 5:
		print(f'{num}', end=' ')
	else:
		print(f'{num}')	
	if cont == 1:
		maior = menor = num
	else:
		if num == 0:
			menor = 0
		if num < menor:
			menor = num
		if num > maior:
			maior = num
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
