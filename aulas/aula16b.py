lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
'''for comida in lanche:
	print(f'Eu vou comer {comida}')
print('Comi muito!')'''
'''for c in range(0, len(lanche)):
	print(f'Eu vou comer {lanche[c]}')
print('Comi Muito!')'''
for pos, comida in enumerate(lanche): # Essa é outra maneira de mostrar o index da Tupla
	print(f'Eu voou comer {comida} na posição {pos}')
