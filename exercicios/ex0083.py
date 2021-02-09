expressao = str(input('Didigite a expressão: ')).strip()
lista = list(expressao)
if lista.count('(') == lista.count(')'):
	print('Sua expressão está válida')
else:
	print('Sua expressão está errada!')
