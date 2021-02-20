def soma (a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B é igual a {s}')


soma(3, 5)
soma(a=8, b=12) # Eu posso explicitar os parâmetros
soma(b=9, a=3) # Se eu explicitar eu posso inclusive fazer em ordem diferente da definição da função
# Essa á maneira de fazer sem função repetindo muito código
# a = 3
# b = 5
# s = a + b
# print(s)
# a = 8
# b = 12
# s = a + b
# print(s)
# a = 9
# b = 3
# s = a + b
# print(s)