# LARGURA E ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, 
# SABENDO QUE CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2m².
from time import sleep
print('=='*20)
print('INFORME A LARGURA E A ALTURA DA PARECE:')
sleep(2)
l = float(input('LARGURA: '))
a = float(input('ALTURA: '))
area = l * a
t = area / 2
print('SUA PAREDE TEM {}x{} E SUA ÁREA É DE {}m².'.format(l,a,area))
print('A QUANTIDADE DE TINTA QUE VC IRÁ PRECIAR USAR É DE {}L.'.format(t))
print('=='*20)