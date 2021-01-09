total = float(input('Informe o preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
	print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(total, total - (total * 0.10)))
elif opcao == 2:
	print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(total, total - (total * 0.05)))
elif opcao == 3:
	print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(total, total))
elif opcao == 4:
	nparcelas = int(input('Quantas parcelas? '))
	vparcelas = float((total + (total * 0.20)) / nparcelas)
	print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'.format(nparcelas, vparcelas))
	print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(total, total + (total * 0.20)))
