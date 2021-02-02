times = ('PALMEIRAS', 'FLAMENGO', 'INTERNACIONAL', 'GRÊMIO',
		'SÃO PAULO', 'ATLÉTICO-MG', 'ATHLETICO', 'CRUZEIRO', 'BOTAFOGO',
		'SANTOS', 'BAHIA', 'FLUMINENSE', 'CORINTHIANS', 'CHAPECOENSE',
		'CEARÁ', 'VASCO', 'SPORT', 'AMÉRICA-MG', 'VITÓRIA', 'PARANÁ')
print('-=' * 15)
print(f'Lista de times do brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros times são: {times[:5]}')
print('-=' * 15)
print(f'Os Quatro últimos são: {times[-4:]}')
print('-=' * 15)
print(f'Os timnes em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print('O Chapecoense está na {}ª Posição'.format(times.index('CHAPECOENSE') + 1))
