trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
trabalhador['nasc'] = int(input('Ano de Nascimento: '))
ctps = int(input('Carteira de Trabalho (0 não tem): '))
if ctps != 0:
	trabalhador['ctps'] = ctps
else:
	trabalhador['ctps'] = 'não cadastrado'
print(trabalhador)
#Antes de incluir os dados colocar como variável e depois inserir no dicionário
#Importa o datetime