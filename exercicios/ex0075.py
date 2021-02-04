resp = (int(input('Digite um número: ')), 
		int(input('Digite outro número: ')), 
		int(input('Digite mais um número: ')), 
		int(input('Digite o último número: '))
		)
print('Os números digitados foram:', end='')
for n in resp:
	print(f' {n}', end='')
print(f'\nO valor 9 apareceu {resp.count(9)} vezes')
if 3 in resp:
	print(f'O valor 3 apareceu a primeira vez na {(resp.index(3) + 1)}ª posição')
else:
	print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for num in resp:
	if num % 2 == 0:
		print(num, end=' ')
