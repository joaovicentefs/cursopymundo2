totI = totM = totF20 = 0
continua = ''
while True:
	print('-' * 40)
	print('{:^40}'.format('CADASTRE UMA PESSOA'))
	print('-' * 40)
	idade = int(input('Idade: '))
	sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
	print('-' * 40)
	continua = str(input('Quer continuar?  [S/N] ')).strip().upper()[0]
	if idade > 18:
		totI += 1
	if sexo == 'M':
		totM += 1
	if sexo == 'F':
		if idade < 20:
			totF20 += 1
	if continua == 'N':
		break
print(f'Total de pessoas com mais de 18 anos: {totI}')
print(f'Número de homens cadastrados: {totM}')
print(f'E o total de mulheres com menos de 20 anos é: {totF20}')
