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
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('=' * 30)		
for i, d in enumerate(boletim, 1):
	print(f'{i:<4}', f'{d[0]:<10}', f'{(d[1] + d[2]) / 2:>8.1f}')
while True:
	print('-' * 30)
	opt = int(input('Mostrar notas de qual aluno? (999 interrompe): ')) - 1
	if opt == 998:
		print('FINALIZANDO...')
		break
	if opt <= len(boletim):
		print(f'Notas de {boletim[opt][0]} são {boletim[opt][1]} e {boletim[opt][2]}')
print('<<< VOLTE SEMPRE >>>')
