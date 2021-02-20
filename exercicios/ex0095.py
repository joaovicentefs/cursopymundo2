elenco = list()
jogador = dict()
gols = list()
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogos = int(input('Quantas partidas {} jogou? '.format(jogador['nome'])))
    for g in range(0, jogos):
        gols.append(int(input(f'Quantos gols na {g + 1}ª? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(jogador['gols'])
    elenco.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for i, j in enumerate(elenco):
    print(f'{i+1:>3} ', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar os dados de qual jogador? (999 para parar) ')) - 1
    if busca == 998:
        break
    if busca > len(elenco):
        print(f'ERRO! Não existe jogador com o código {busca + 1}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {elenco[busca]["nome"]}:')
        for i, g in enumerate(elenco[busca]['gols']):
            if g > 1:
                print(f'   No jogo {i + 1} fez {g} gols.')
            elif g == 1:
                print(f'   No jogo {i + 1} fez {g} gol.')
            elif g == 0:
                print(f'   No jogo {i + 1} não fez nenhum gol!.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
