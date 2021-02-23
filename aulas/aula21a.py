# Exemplo de Return:
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f #Os returns podem ser valores


# n = int(input('Digite o valor que você gostaria de calcular o fatorial: '))
# print(f'O Fatorial de {n} é {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os Resultados são {f1}, {f2} e {f3}')