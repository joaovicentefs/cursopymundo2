resp = (int(input('Digite um número: ')), 
		int(input('Digite outro número: ')), 
		int(input('Digite mais um número: ')), 
		int(input('Digite o último número: '))
		)
print(f'O valor 9 apareceu {resp.count(9)} vezes')
print(f'O valor 3 apareceu a primeira vez na {(resp.index(3) + 1)}ª posição')
print('Os valores pares digitados foram: ', end='')
for num in resp:

	if num % 2 == 0:
		print(num, end=' ')
