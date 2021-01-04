nome = str(input('Qual o seu o nome? '))
if nome == 'João':
	print('Que nome bonito!')
elif nome == 'José' or  nome == 'Maria' or nome == 'Paulo':
	print('Seu nome é bem Popular no Brasil!')	
else:
	print('Seu nome é  bem normal!')
print('Tenha um bom dia {}'.format(nome))
