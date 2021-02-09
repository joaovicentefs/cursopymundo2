teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) # Sem usar o '[:]' ele não faria uma cópia e sim uma conexão entre as listas
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
