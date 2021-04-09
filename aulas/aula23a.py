try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('Execução interrompida pelo usuário ou o usuário preferiu não informar os dados')
else: # Aparece caso o não apresente nenhum "erro"
    print(f'O resultado é {r:.1f}')
finally: # Aparece com ou sem o erro.
    print('volte sempre, muito obrigado!')