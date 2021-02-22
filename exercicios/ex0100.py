from random import  randint
from time import sleep
numeros = []


def sorteia(lst):
    print('Sorteando 5 valores da lista: ', end='')
    for n in range(0, 5):
        num = randint(0, 10)
        lst.append(num)
        print(num, end=' ')
        sleep(0.3)
    print('PRONTO!')


def somaPar(lst):
    somap = 0
    for n in lst:
        if n % 2 == 0:
            somap += n
    print(f'Somando os valores pares de {lst}, temos {somap}')


sorteia(numeros)
somaPar(numeros)
