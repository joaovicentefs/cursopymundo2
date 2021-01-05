vCasa = float(input('Valor da Casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
tempo = int(input('Quantos anos de financiamento? '))
prestacao = vCasa / (tempo * 12)
# Quebrei o print em dois apenas para mostrar o uso do Recurso end= que deixa dois prints em uma linha só
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(vCasa, tempo), end='')
print(' a prestação será de R$ {:.2f}'.format(prestacao))
if prestacao <= salario * (30 /100):
	print('Empréstimo APROVADO!')
else:
	print('Empréstimo REPROVADO')
