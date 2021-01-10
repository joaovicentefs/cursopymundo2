#Exemplo para construção de um contador regressivo simpples
#Uso do terceiro valor dentro do Range que serve como 'incrementador'
n = int(input('Digite um valor positivo: '))
for c in range(n, -1, -1): # O segundo '-1' é que permite a contagem regressiva funcionar
	print(c)
print('FIM')