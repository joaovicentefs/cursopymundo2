def aumentar(num=0, perc=0, formato=False):
    f = num + (num * (perc/100))
    return f if formato is False else moeda(f)


def diminuir(num=0, perc=0, formato=False):
    f = num - (num * (perc/100))
    return f if formato is False else moeda(f)


def dobro(num=0, formato=False):
    d = num * 2
    return d if formato is False else moeda(d)


def metade(num=0, formato=False):
    m = num / 2
    return m if formato is False else moeda(m)


def moeda(num=0, moeda='R$'):
    return f'{moeda} {num:>.2f}'.replace('.', ',')

def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(preco, taxar, True)}')
    print('-' * 30)