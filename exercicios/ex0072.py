extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
numero = 21
while numero not in range(0, 21):
	numero = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {extenso[numero]}')
