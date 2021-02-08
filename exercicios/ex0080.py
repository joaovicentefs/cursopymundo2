lista = list()
for n in range(0, 5):
	item = int(input('Digite um valor: '))
	if n == 0 or item > lista[-1]:
		lista.append(item)
		print('Adicionado ao final da lista')
	else:
		pos = 0
		while pos < len(lista):
			if item <= lista[pos]:
				lista.insert(pos, item)
				print(f'Adicionado na posição {pos} da lista')
				break
			pos +=1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')