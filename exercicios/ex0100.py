from random import  randint
from time import sleep
numeros = []


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for n in range(0, 5):
        num = randint(0, 10)
        numeros.append(num)
        print(num, end=' ')
    print('PRONTO!')


def somaPar(lst):
    somap = 0
    for n in lst:
        if n % 2 == 0:
            somap += n
    print(f'Somando os valores pares de {lst}, temos {somap}')


sorteia()
somaPar(numeros)