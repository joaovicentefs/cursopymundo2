from datetime import date
menor = 0
maior = 0
for c in range(1,8):
	ano = int(input('Em que ano a {}ª nasceu? '.format(c)))
	if date.today().year - ano < 18:
		menor += 1
	else:
		maior += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))