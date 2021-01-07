from datetime import date
hoje = date.today().year
nasc = int(input('Informe seu ano de nascimento: '))
idade = hoje - nasc
txt_padrao = 'Sua Categoria:'
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
	print(txt_padrao, 'MIRIM')
elif 9 < idade <= 14:
	print(txt_padrao, 'INFANTIL')
elif 14 < idade <= 19:
	print(txt_padrao, 'JÚNIOR')
elif 19 < idade <= 25:
	print(txt_padrao, 'SÊNIOR')
elif idade > 25:
	print(txt_padrao, 'MASTER')
