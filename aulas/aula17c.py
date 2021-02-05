a = [2, 3, 4, 7]
#b = a #NQuando igualamos duas listas é criada uma conexão entre elas
b = a[:] # Neste caso eu estou fazendo uma cópia de a em B e assim se algo for modificado en uma não será refletido na outra, porque elas não estão conectadas
b[2] = 8 # Neste caso mesmo que eu altere apenas em b como as listas estão conectadas a nmudança será espelhada
print(f'Lista A: {a}')
print(f'Lista B: {b}')
