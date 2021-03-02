def aumentar(num=0, perc=0):
    f = num + (num * (perc/100))
    return f


def diminuir(num=0, perc=0):
    f = num - (num * (perc/100))
    return f


def dobro(num=0):
    d = num * 2
    return d


def metade(num=0):
    m = num / 2
    return m


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')