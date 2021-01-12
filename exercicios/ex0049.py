n = int(input('Digite o número: '))
print('-=' * 5)
for c in range(1,11):
	print('{} X {:2} = {}'.format(n, c, (n * c)))
print('-=' * 5)
