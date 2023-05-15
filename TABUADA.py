# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E MOSTRE NA TELA A SUA TABUADA
from time import sleep
nome = ('TABUADA')
print('x  '*18)
print('{:=^50}'.format(nome))
print('ESCOLHA UM NÚMERO PARA VER SUA TABUADA')
sleep(1)
e = int(input('QUAL NÚMERO: \n>>> '))
print('x  '*18)
e0 = e * 0
e1 = e * 1
e2 = e * 2
e3 = e * 3
e4 = e * 4
e5 = e * 5
e6 = e * 6
e7 = e * 7
e8 = e * 8
e9 = e * 9 
e10 = e * 10
print('{:=^50}'.format(nome))
print('{}  x  0 = {}'.format(e,e0))
print('{}  x  1 = {}'.format(e,e1))
print('{}  x  2 = {}'.format(e,e2))
print('{}  x  3 = {}'.format(e,e3))
print('{}  x  4 = {}'.format(e,e4))
print('{}  x  5 = {}'.format(e,e5))
print('{}  x  6 = {}'.format(e,e6))
print('{}  x  7 = {}'.format(e,e7))
print('{}  x  8 = {}'.format(e,e8))
print('{}  x  9 = {}'.format(e,e9))
print('{}  x 10 = {}'.format(e,e10))
print('x  '*18)
