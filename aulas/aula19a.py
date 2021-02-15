pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# print(pessoas)
# print(pessoas['nome'])
# print(pessoas['idade'])
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = float(90)
for d in pessoas.keys():
	print(d)
for d in pessoas.values():
	print(d)
for k, v in pessoas.items(): #Substitui o o uso do Enumerate que usamos em Tuplas e Listas
	print(f'{k} = {v}')
