valores = list() # Começando uma lista vazia, poderia usar apenas os Colchetes vazios
'''valores.append(5)
valores.append(9)
valores.append(4)'''
for cont in range(0, 5):
	valores.append(int(input('Digite um valor: '))) # Inserindo valores na lista com dados do usuário
# for v in valores:
	#print(f'{v}...', end='')
for c, v in enumerate(valores):
	print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')
