from datetime import date
anoNascimento = int(input('Ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
if idade < 18:
	print('''Quem nasceu em {} tem {} anos em {}.
	Ainda faltam {} ano(s) para o alistamento.
	Seu alistamento será em {}'''.format(anoNascimento, idade, anoAtual, 18 - idade, anoAtual + (18 - idade)))
elif idade > 18:
	print('''Quem nasceu em {} tem {} anos em {}.
	Você já deveria ter se alistado há {} ano(s).
	Seu alistamento foi em {}.'''.format(anoNascimento, idade, anoAtual, abs(18 - idade), anoAtual - (idade - 18)))
else:
	print('''Quem nasceu em {} tem {} anos em {}.
	Você tem que se alistar IMEDIATAMENTE!'''.format(anoNascimento, idade, anoAtual))