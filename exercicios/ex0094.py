cadastro = dict()
pessoas = list()
soma = media = 0
while True:
    cadastro['nome'] = str(input('Nome: '))
    while True:
        cadastro['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if cadastro['sexo'] in 'MF':
            break
        else:
            print('ERRO!Por favor digite apenas M ou F.')
    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']
    pessoas.append(cadastro.copy())
    cadastro.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = soma / len(pessoas)
print(f'B) A média de idade é de {media:.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} |', end=' ')
print()
print('D) Lista das pessoas que estão acima da média:')
for i in pessoas:
    if i['idade'] > media:
        for k, v in i.items():
            print(f'{k} = {v};', end=" ")
        print()
print('<< ENCERRADO >>')
