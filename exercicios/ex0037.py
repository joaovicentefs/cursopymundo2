num = int(input('Digite um número interiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
options = int(input('Sua opção: '))
if options == 1:
	print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
elif options == 2:
	print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)))
elif options == 3:
	print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))
else:
	print('Escolha uma opção de conversão válida!')