def aumentar(num, perc):
    f = num + (num * (perc/100))
    return f'Aumentando {perc}%, temos R$ {f:.2f}'


def diminuir(num, perc):
    f = num - (num * (perc/100))
    return f'Diminuindo {perc}, temos R$ {f:.2f}'


def dobro(num):
    d = num * 2
    return f'O dobro de R$ {num} é R$ {d:.2f}'


def metade(num):
    m = num / 2
    return f'A metade de R$ {num} é R$ {m:.2f}'
