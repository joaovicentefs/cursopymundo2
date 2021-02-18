jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input('Quantas partidas {} jogou? '.format(jogador['nome'])))
for g in range(0, partidas):
    gols.append(int(input(f'Quantos gols na {g + 1}ª? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O Campo {k} tem o valor {v}')
print('-=' * 30)
print('O jogador {} jogou {} partidas.'.format(jogador['nome'], partidas))
for i, v in enumerate(gols):
    if v > 1:
        print(f'   => Na partida {i + 1}, fez {v} gols.')
    elif v == 1:
        print(f'   => Na partida {i + 1}, fez {v} gol.')
    elif v == 0:
        print(f'   => Na partida {i + 1}, Não fez nenhum gol!')
print(f'Foi um total de {sum(gols)} gols.')