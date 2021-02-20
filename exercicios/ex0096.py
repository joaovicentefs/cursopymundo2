def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno com {larg} x {comp} é de {a}m².')


print(f'{"Controle de Terrenos":^30}')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
