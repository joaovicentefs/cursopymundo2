num = [2, 5, 9, 1]
num[2] = 0 #Lista podem ser modificadas, alterando, adicionando ou removendo elementos
num.append(7) # Adiciona um valor no final da lista
# num.sort() # Ordena os elementos da lista de maneira crescente
num.sort(reverse=True) # Ordena os elementos de maneira decrescente
num.insert(2, 0) # Neste caso ele vai inserir o valor 0 no index 2
num.pop() #Remove o últimno valor da lista, se colocarmos a referencia de index na lista ele funciona também
num.insert(1, 2)
num.remove(2) # Quando o item a ser remnovido aparece mais de uma vez na lista ele vai apagar a primeira ocorrência
if 4 in num:
	num.remove(4) # Caso o valor não existe na listaq ele vai acusar um erro, para resolver isso podemos colocar umn if
else:
	print('Não encontrei o valor 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')
