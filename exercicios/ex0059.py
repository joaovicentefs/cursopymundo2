from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = int()
resultado = 0
maior = 0
while opcao != 5:
	print('''
	[ 1 ] somar
	[ 2 ] multiplicar
	[ 3 ] maior
	[ 4 ] novos números
	[ 5 ] sair do programa''')
	opcao = int(input('>>>>> Qual é a sua opção: '))
	if opcao == 1:
		resultado = n1 + n2
		print('A Soma entre {} + {} é {}'.format(n1, n2, resultado))
		print('=-' * 15)
	elif opcao == 2:
		resultado = n1 * n2
		print('A Multiplicação entre {} x {} é {}'.format(n1, n2, resultado))
		print('=-' * 15)
	elif opcao == 3:
		if n1 == n2:
			print('Não existe maior, os dois números são iguais!')
		elif n2 > n1:
			maior = n2
			print('O maior número é {}.'.format(maior))
		else:
			maior = n1
			print('O maior número é {}.'.format(maior))
	elif opcao == 4:
		n1 = int(input('Primeiro valor: '))
		n2 = int(input('Segundo valor: '))
	elif opcao != [1, 2, 3, 4, 5]:
		print('Opção inválida! Tente novamente.')
print('Finalizado...')
print('Programa encerrado!')