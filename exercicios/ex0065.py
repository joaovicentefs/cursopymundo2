maior = menor = cont = soma = 0
resp = 's'
while resp in 'Ss':
	num = int(input('Digite um número: '))
	soma += num
	cont +=1
	resp = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
	if cont == 1:
		maior = menor = num # Aqui é o que u estava errando no exrecício
	else: # Aqui também
		if num > maior:
			maior = num
		elif num < menor:
			menor = num		
media = soma / cont
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))