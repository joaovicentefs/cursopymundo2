from datetime import date
hoje = date.today().year
nasc = int(input('Informe seu ano de nascimento: '))
idade = hoje - nasc
txt_padrao = 'Sua Categoria:'
print('O atleta tem {} anos.'.format(idade))
'''Não preciso usar o 9 < no primeiro elif porque se ele chegou nesta condição é que ele passou 
pela outra, com isso podemos simplificar todos os elif'''
if idade <= 9:
	print(txt_padrao, 'MIRIM')
elif idade <= 14:
	print(txt_padrao, 'INFANTIL')
elif idade <= 19:
	print(txt_padrao, 'JÚNIOR')
elif idade <= 25:
	print(txt_padrao, 'SÊNIOR')
elif idade > 25:
	print(txt_padrao, 'MASTER')
