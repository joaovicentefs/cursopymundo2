# cont = 0
print('='*30)
txt = '10 TERMOS DE UMA PA'
x = txt.center(30,' ')
print(x)
print('='*30)
'''num = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
for c in range(num, 9999, raz):
	cont += 1
	if cont <= 10:
		print(c, '--> ', end='')
print('ACABOU')'''
# Versão do Guanabara
primeiro = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
decimo = primeiro + (10 -1) * raz
for c in range(primeiro, decimo + raz, raz):
	print(c, end=' --> ')
print('ACABOU')