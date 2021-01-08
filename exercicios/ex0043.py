peso = float(input('Qual é seu peso? (Kg): '))
altura = float(input('Qual é sua altura? (m): '))
imc = float(peso / pow(altura, 2))
print('O IMC desta pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
	print('Cuidado você está ABAIXO DO PESO NORMAL')
elif 18.5 <= imc < 25:
	print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
	print('Atenção! Você está com SOBREPESO! Alimente-se melhor.')
elif 30 <= imc < 40:
	print('Alerta vermelho! Você já está na fase de OBSEDIDADE')
elif imc >= 40:
	print('Seu caso é grave. Você está na faixa de OBESIDADE MÓRBIDA, procure um médico!')