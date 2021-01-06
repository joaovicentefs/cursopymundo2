num = int(input('Digite um número interiro: '))
#Colocando três aspas simples no print é possível fazer múltiplas linhas
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
options = int(input('Sua opção: '))
'''Utilizado o conhecimento de fatiamento de string para ignorar
os dois primeiros dígitos que servem apenas para identificar qual a base numérica'''
if options == 1:
	print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif options == 2:
	print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif options == 3:
	print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
	print('Escolha uma opção de conversão válida!')