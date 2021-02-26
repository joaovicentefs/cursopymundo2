def lin(txt):
    tlinha = len(txt) + 4
    print('~' * tlinha)
    print(f"  {txt}  ")
    print('~' * tlinha)


while True:
    lin('SISTEMA DE AJUDA PyHELP')
    funlib = str(input('Função ou Biblioteca? (Digite FIM para encerrar) ')).strip().lower()
    if funlib == 'fim':
        break
    lin(f'Acessando o manual do comando \'{funlib}\'')
    help(funlib)
