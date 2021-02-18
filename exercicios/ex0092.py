from datetime import datetime
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
trabalhador['idade'] = datetime.now().year - nasc
ctps = int(input('Carteira de Trabalho (0 não tem): '))
if ctps != 0:
	trabalhador['ctps'] = ctps
	trabalhador['contratacao'] = int(input('Ano de contratação: '))
	trabalhador['salario'] = float(input('Salário: R$ '))
	trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratacao'] + 35) - datetime.now().year)
else:
	trabalhador['ctps'] = 'não cadastrado'
print('-=' * 30)
for k, v in trabalhador.items():
	print(f'- {k} tem o valor {v}')