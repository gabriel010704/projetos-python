from time import sleep
usuario = (1,2,3,4,5,6,7)
opcao = False
while opcao == False:
    print('+  -  X  ÷  %  ^  √  '*4)
    usuario = int(input('''QUAL DAS OPERAÇÕES DESEJA REALIZAR:

[ 1 ] ADIÇÃO
[ 2 ] SUBTRAÇÃO
[ 3 ] MULTIPLICAÇÃO
[ 4 ] DIVISÃO
[ 5 ] PORCENTAGEM
[ 6 ] POTÊNCIA
[ 7 ] RAIZ 

DIGITE AQUI: '''))
    if usuario == 1:
        print('+  '*20)
        n1 = float(input('INFORME UM NÚMERO: '))
        n2 = float(input('INFORME OUTRO NÚMERO: '))
        r = n1 + n2
        print('O RESULTADO DE {} + {} = {}'.format(n1,n2,r))
        print('+  '*20)
        break
    elif usuario == 2:
        print('-  '*20)
        n1 = float(input('INFORME UM NÚMERO:'))
        n2 = float(input('INFORME OUTRO NÚMERO:'))
        r = n1 - n2
        print('O RESULTADO DE {} - {} = {}'.format(n1,n2,r))
        print('-  '*20)
        break
    elif usuario == 3:
        print('X  '*20)
        n1 = float(input('INFORME UM NÚMERO:'))
        n2 = float(input('INFORME OUTRO NÚMERO:'))
        r = n1 * n2
        print('O RESULTADO DE {} x {} = {}'.format(n1,n2,r))
        print('X  '*20)
        break
    elif usuario == 4:
        print('÷  '*20)
        n1 = float(input('INFORME UM NÚMERO:'))
        n2 = float(input('INFORME OUTRO NÚMERO:'))
        r = n1 / n2
        print('O RESULTADO DE {} ÷ {} = {:.2f}'.format(n1,n2,r))
        print('÷  '*20)
        break
    elif usuario == 5:
        print('%  '*20)
        n1 = float(input('INFORME QUANTOS POR CENTO:'))
        n2 = float(input('INFORME UM NÚMERO:'))
        r = n1 * n2
        s = r / 100
        print('{}% DE {} É {:.2f}'.format(n1,n2,s))
        print('%  '*20)
        break
    elif usuario == 6:
        print('^  '*20)
        n1 = float(input('DIGITE UM NÚMERO:'))
        n2 = float(input('DIGITE OUTRO NÚMERO ELEVADO:'))
        s = n1 ** n2
        print('{} ELEVADO {} = {:.3f}'.format(n1,n2,s))
        print('^  '*20)
        break
    elif usuario == 7:
        print('√  '*20)
        n1 = float(input('DIGITE UM NÚMERO:'))
        n2 = float(input('DIGITE OUTRO NÚMERO:'))
        r = n1**(1/n2)
        print('A RAIZ DE {} = {:.3f}'.format(n1,r))
        print('√  '*20)
        break
    else:
        print('''OPÇÃO NÃO ENCONTRADA!
ESCOLHA UMA DAS OPÇÕES ACIMA PARA PROSSEGUIR.''')
        sleep(2)
        opcao == True





# (+) ADIÇÃO
# (-) SUBTRAÇÃO
# (*) MULTIPLICAÇÃO
# (/) DIVISÃO
# (**) POTÊNCIA
# (//) DIVISÃO INTEIRA
# (%) RESTO DA DIVISÃO

# ORDEM DE PRECEDÊNCIA 
# 1° - [ () ]
# 2° - [ ** ]
# 3° - [ * / // % ]
# 4° - [ + - ]