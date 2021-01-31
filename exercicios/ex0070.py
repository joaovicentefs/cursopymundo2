gasto = mais_caro = 0
item_barato = ' '
print('-' * 40)
print('{:^40}'.format('LOJÃO DO JOÃO'))
print('-' * 40)
while True:
	produto = str(input('Nome do produto: ')).strip().lower()
	preco = float(input('Preço: R$ '))
	mais_barato = preco
	gasto += preco
	resp = ' '
	if preco > 1000:
		mais_caro += 1
	if preco < mais_barato:
		mais_barato = preco
		item_barato = produto
	while resp not in 'SN':
		resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
	if resp == 'N':
		break
print(f'O total da compra foi R$ {gasto:.2f}')
print(f'Esta é a quantidade de produtos acima de R$ 1.000,00: {mais_caro}')
print(f'O produto mais barato foi {item_barato} que custa R$ {mais_barato:.2f}')
