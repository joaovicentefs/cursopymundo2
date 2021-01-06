from datetime import date
anoNascimento = int(input('Ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(anoNascimento, idade, anoAtual))
if idade < 18:
	print('''Ainda faltam {} ano(s) para o alistamento.
	Seu alistamento será em {}'''.format(18 - idade, anoAtual + (18 - idade)))
elif idade > 18:
	print('''Você já deveria ter se alistado há {} ano(s).
	Seu alistamento foi em {}.'''.format(abs(18 - idade), anoAtual - (idade - 18)))
elif idade < 18:
	print('Você tem que se alistar IMEDIATAMENTE!')
