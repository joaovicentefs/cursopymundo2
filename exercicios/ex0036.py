vCasa = float(input('Valor da Casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
tempo = int(input('Quantos anos de financiamento? '))
prestacao = vCasa / (tempo * 12)
print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}'.format(vCasa, tempo, prestacao))
if prestacao <= salario * (30 /100):
	print('Empréstimo APROVADO!')
else:
	print('Empréstimo REPROVADO')
