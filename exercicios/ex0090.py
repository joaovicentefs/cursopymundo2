ficha = dict()
ficha['nome'] = str(input('Nome: '))
ficha['media'] = float(input(f'Média de {ficha["nome"]}: '))
if ficha['media'] >= 6.0:
	ficha['status'] = 'Aprovado'
else:
	ficha['status'] = 'Reprovado'
print('-=' * 30)
print('- ', f'Nome é igual a {ficha["nome"]}')
print('- ', f'Ḿédia é igual a {ficha["media"]}')
print('- ', f'Situação é igual a {ficha["status"]}')
