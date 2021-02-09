expressao = str(input('Didigite a expressão: ')).strip()
# minha versão
'''lista = list(expressao)
if lista.count('(') == lista.count(')'):
	print('Sua expressão está válida')
else:
	print('Sua expressão está errada!')'''
# Versão do Guanabara
lista = list()
for simb in expressao:
	if simb == '(':
		lista.append('(')
	elif simb == ')':
		if len(lista) > 0:
			lista.pop()
		else:
			lista.append(')')
			break
if len(lista) == 0:
	print('Sua expressão está válida')
else:
	print('Sua expressão está errada!')
