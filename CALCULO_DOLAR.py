
nome = ('--CALCULO DE DÓLAR--')
print(    '{:=^51}'.format(nome))
print('$  '*17)
n = float(input('QUANTOS R$ VOCÊ TEM?\n>>>R$ '))
d = n / 5.06
print('-'*43) 
print('COM {:.2f} R$ VOCÊ PODE COMPRAR \n>>> {:.2f} US$'.format(n,d))
print('$  '*17)
