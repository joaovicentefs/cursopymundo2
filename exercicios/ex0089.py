boletim = list()
dados = list()
while True:
	dados.append(str(input('Nome: ')).strip().capitalize())
	dados.append(float(input('Nota 1: ')))
	dados.append(float(input('Nota 2: ')))
	boletim.append(dados[:])
	dados.clear()
	resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
	if resp == 'N':
		break
print('-=' * 30)
print('Nº ', '{:<10}'.format("NOME"), 'MÉDIA')
print('=' * 30)		
for i, d in enumerate(boletim, 1):
	print(f'{i}', f'{d[0]:<14}', f'{(d[1] + d[2]) / 2:>}')
print('-' * 30)
while True:
	opt = int(input('Mostrar notas de qual aluno? (999 interrompe): ')) - 1
	if opt == 999:
		break
	print(f'Notas de {boletim[opt][0]} são {boletim[opt][1]} e {boletim[opt][2]}')

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
