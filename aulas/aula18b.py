galera = [['João', 35], ['Fernanda', 38], ['Gregório', 3], ['Frederico', 1]]
#print(galera)
for pessoa in galera:
	#print(pessoa)
	if pessoa[1] <= 1:
		print(f'{pessoa[0]} tem {pessoa[1]} ano')	
	else:
		print(f'{pessoa[0]} tem {pessoa[1]} anos')
