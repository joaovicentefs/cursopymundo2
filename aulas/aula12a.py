# Aprendendo condições aninhadas
nome = str(input('Qual o seu o nome? '))
if nome == 'João':
	print('Que nome bonito!')
elif nome == 'José' or  nome == 'Maria' or nome == 'Paulo':
	print('Seu nome é bem Popular no Brasil!')
elif nome in 'Ana Maria Paula Gabriela':
	print('Belo nome feminino')
else:
	print('Seu nome é  bem normal!')
print('Tenha um bom dia {}'.format(nome))
