try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro: # Aparece quando "erro" acontece
    print(f'ERRO. O problema encontrado foi {erro.__class__}')
else: # Aparece caso o não apresente nenhum "erro"
    print(f'O resultado é {r:.1f}')
finally: # Aparece com ou sem o erro.
    print('volte sempre, muito obrigado!')