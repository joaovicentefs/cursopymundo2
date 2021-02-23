def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: Parâmetro Opicional, valor padrão False se for True mostra o Calculo.
    :return: Retorna o fatorial calculado de um número n.
    """
    f = 1
    for num in range(n, 0, -1):
        if show:
            print(num, end='')
            if num > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= num
    return f


print(fatorial(8))
#help(fatorial)
