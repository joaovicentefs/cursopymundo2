velho = 0
totid =0
nvelho = ''
cont = 0
for pess in range(1,5):
	print('---- {}ª PESSOA ----'.format(pess))
	nome = str(input('Nome: ')).title()
	idade = int(input('Idade: '))
	sexo = str(input('Sexo [M/F]: ')).upper()
	totid += idade
	if pess == 1 and sexo == 'M':
		velho = idade
	elif sexo == 'M' and idade > velho:
		velho = idade
		nvelho = nome
	elif sexo == 'F' and idade < 20:
		cont += 1
media = float(totid / 4)
print('A média de idade do grupo é de {:.1f} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(velho, nvelho))
print('Ao todo temos {} mulheres com menos de 20 anos.'.format(cont))
