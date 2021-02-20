def contador(* num): #Empacotamento de parametros, ele neste caso ele me permite colcoar quanto parametrosd eu quiser
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')
contador(1, 9, 8, 5)
contador(0, 2, 0, 6, 5, 0, 8, 6, 5, 4, 8)
contador(2)