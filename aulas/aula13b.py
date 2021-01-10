#Exemplo de uso do for usando uma entrada do usuário como parte de passagem do for
n = int(input('Digite um número: '))
for c in range(0, n+1): # É preciso colocar o '+1' porque o python desconsidera o último valor
	print(c)
print('FIM!')