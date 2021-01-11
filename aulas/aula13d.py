#Usando estrutura de for a nosso favor com múltiplas variáveis:
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))# Passo é a mesma coisa que ritmo ou cadência
for c in range(i, f+1, p):
	print(c)
print('FIM!')
