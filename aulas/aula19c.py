estado = dict()
brasil = list()
for c in range(0, 3):
	estado['nome'] = str(input('Nome do Estado: '))
	estado['uf'] = str(input('Sigla do Estado: '))
	brasil.append(estado.copy()) # NO Dicionário usamos a função copy ao invés do parametro "[:]"
for e in brasil:
	# for k, v in e.items():
	# 	print(f'{k} é {v}')
	for v in e.values():
		print(v, end=' ')
	print()