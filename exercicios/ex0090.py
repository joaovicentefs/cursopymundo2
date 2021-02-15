ficha = dict()
ficha['nome'] = str(input('Nome: '))
ficha['media'] = float(input(f'Média de {ficha["nome"]}: '))
if ficha['media'] >= 7.0:
	ficha['status'] = 'Aprovado'
elif 5 <= ficha['media'] < 7:
	ficha['status'] = 'Recuperação'
else:
	ficha['status'] = 'Reprovado'
print('-=' * 30)
for k, v in ficha.items():
	print(f'  - {k} é igual a {v}.')
