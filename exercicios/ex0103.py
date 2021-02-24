def ficha(nome='<desconhecido>', gol=0):
    print(f'O Jogador {nome} fez {gol} gol(s) no campeonato')


n = str(input('Nome do jogador: '))
g = str(input('Número de gols: ')) # usa tipo string para aceitar o valor em branco
if g.isnumeric():# Aqui valido sem tem números no input
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
