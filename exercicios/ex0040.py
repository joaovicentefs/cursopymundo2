
nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if media > 6.9:
	print('O aluno está APROVADO.')
elif media >= 5.0 and media <= 6.9:
	print('O aluno está em RECUPERAÇÃO.')
elif media < 5.0:
	print('O aluno está REPROVADO.')