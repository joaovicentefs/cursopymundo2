num = 0
soma = num
cont = 0
while num != 999:
	num = int(input('Digite um número [999 para parar]: '))
	if num != 999:
		soma += num
		cont += 1
	else:
		soma = soma
		cont = cont
print('Foram digitados {} números e a soma deles é {}.'.format(cont, soma))