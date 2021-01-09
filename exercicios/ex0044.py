print('{:=^40}'.format(' LOJAS UPSITES '))
compras = float(input('Informe o preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
	total = compras - (compras * 0.10) 
elif opcao == 2:
	total = compras - (compras * 0.05)
elif opcao == 3:
	total = compras
	parcela = total / 2
	print('Sua compra será parcela em 2x de R$ {:.2f} SEM JUROS.'.format(parcela))
elif opcao == 4:
	total = compras + (compras * 0.20)
	nparcelas = int(input('Quantas parcelas? '))
	vparcelas = float((compras + (compras * 0.20)) / nparcelas)
	print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'.format(nparcelas, vparcelas))
else:
	total = compras
	print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(compras, total))