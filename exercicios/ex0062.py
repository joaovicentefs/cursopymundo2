primeiro = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
cont = 1
termo = primeiro
contador_termo = 1
mais = 10
total = 0
while mais != 0:
	total += mais
	while cont <= total:
		print('{}'.format(termo), end=' --> ')
		termo += raz
		cont += 1
	print('PAUSA')
	mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
