#Essa é versão nova do exercício 35 com atualizações usando condições
print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
#O Python permite fazer a comparação direta sem precisar usar o AND entre as comparações    
    if l1 == l2 == l3:
    	print('EQUILÁTERO!')
 		#Neste caso tivemos que comparar todos, incluindo o l1 de novo porque a igualdade é inclusiva a diferença não.
		#Porque o l1 pode ser diferente de l2 mas ser igual a l3, mas se l1 for igual a l2 e l2 igual a l3, logo l1 é igual a l3
    elif l1 != l2 != l3 !=l1:
    	print('ESCALENO!')
    else:
    	print('ISÓCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
