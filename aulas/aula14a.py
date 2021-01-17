# O While é mais versátil
# É possível usar ele com ou sem um limite, ao contrário do range
# O while usa o teste lógico para determinar a repetição ou não
# VERSÃO USANDO for:
'''for c in range(1,11):
	print(c)
print('FIM!')'''
# VERSÃO com while
c = 1
while c < 11: # A condicional é chamado de flag ou condição de parada
	print(c)
	c += 1
print('FIM!')