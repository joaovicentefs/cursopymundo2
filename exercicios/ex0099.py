from time import sleep
def maior(* num):
    cont = m = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    sleep(1)
    for v in num:
        print(f'{v} ', end='')
        cont += 1
        sleep(0.3)
        if cont == 1:
            m = v
        else:
            if v > m:
                m = v
    if cont == 1:
        print(f'Foi informado {cont} valor ao todo')
    elif cont > 1:
        print(f'Foram informados {cont} valores ao todo')
    else:
        print('Nenhum valor foi informado!')
    print(f'O maior valor foi {m}.')



maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(6)
maior()
