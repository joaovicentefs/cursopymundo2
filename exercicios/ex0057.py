sex = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sex not in 'MmFf':
	print('Dados inválidos.', end=' ')
	sex = str(input('Por favor inform seu sexo: '))
print('Sexo {} registrado com sucesso'.format(sex))
