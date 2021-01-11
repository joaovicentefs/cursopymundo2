#Usando o for para fazer repetição de input
'''for c in range(0,4):
	n = int(input('Digite um valor: '))
print('Fim')'''
#Abaixo a versão mas bem trabalhada do exercício com mais funções
soma = 0
for c in range(0,4):
	n = int(input('Digite um valor: '))
	soma = soma + n #QUue poderia ser represetando por s += n
#O que esse script faz é somar de maneira cumulativa os valores de cada input
print('O Somatório de todos os valores foi {}'.format(soma))
