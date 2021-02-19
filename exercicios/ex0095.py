elenco = list()
jogador = dict()
gols = list()
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['partidas'] = int(input('Quantas partidas {} jogou? '.format(jogador['nome'])))
    for g in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols na {g + 1}ª? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(jogador['gols'])
    elenco.append(jogador.copy())
    jogador.clear()
    gols.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(elenco)
print(f'{"cod":<4}{"nome":<15}{"gols":<15}{"total":>5}')
print('-' * 40)
for i, j in enumerate(elenco):
    print(f'{i:<4}', end=' ')
    for k, v in j.items():
        if k == 'nome':
            print(f'{v:<15}', end=' ')
        if k == 'gols':
            print(v, f'{"":<5}', end=' ')
        if k == 'total':
            print(f'{v:>3}', end=' ')
    print()
