cont = soma = 0
resp = 'S'
num = 0
maior = menor = num
while resp in 'Ss':
	num = int(input('Digite um número: '))
	resp = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
	soma += num
	cont +=1
	if num > maior:
		maior = num
	if menor > num:
		menor = num
media = soma / cont
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))