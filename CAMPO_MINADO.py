from random import randint

from time import sleep

sim = 1
nao = 2
vamos_jogar = 2

jogar = False
while jogar == False:
    print('--'*20)
    print('''BEM VINDO AO JOGO DO CAMPO DAS FLORES''')
    sleep(2)
    
    print('--'*20)

    print('''AVISO: ALGUMAS FLORES ESTÃO BEM ESPLOSIVAS.
CUIDADO ONDE PISA !!!''')
    print('--'*20)
    sleep(2)
    print('''OPÇÕES:
1 - SIM 
2 - NÃO''')
    vamos_jogar = int(input('''GOSTÁRIA DE DAR UM PASSEIO NO CAMPO DE FLORES?

DIGITE AQUI:'''))
    print('--'*20)
    if vamos_jogar == 1:
        print('''ÓTIMO, VAMOS COMEÇAR. 
SÓ TOME CUIDADE ONDE PISA''')
        jogar = True
        break
    elif vamos_jogar == 2:
        print('VOLTE QUANDO QUISER DAR UM PASSEIO.')
    else:
        print('ESCOLHA INVÁLIDA')
        sleep(2)
jogo = False
while jogo == False:
      
    esquerda = 1
    centro = 2
    direira = 3
    print('--'*20)
    print()
    print('''COMPLETE AS 3 FASES PARA GANHAR E CHEGAR DO OUTRO LADO''')
    print()
    print('--'*20)

    sleep(3)
    print('''OPÇÕES PARA CAMINHAR:
1 - ESQUERDA 
2 - PARA FRENTE
3 - DIREITA''')
    print('--'*20)
    sleep(2)
    print('ESCOLHA COM SABEDORIA O CAMINHO QUE IRÁ FAZER')
    print('--'*20)
    sleep(2)

    print('''FASE 1''')

    print('--'*20)
    sleep(2)
    bomba = randint (1,3)

    jogador = int(input('''PARA QUAL DIREÇÃO VAMOS

DIGITE AQUI:'''))

    if bomba == 1:
        if jogador == 1:
            print('VOCÊ PISOU EM UMA BOMBA')
            print('3')
            sleep(1)
            print('2')
            sleep(1)
            print('1')
            sleep(1)
            print('''BOOOOOOM!!!
            
VOCÊ MORREU.''')
            break
        elif jogador == 2:
            print('''MUITO BEM, ESCOLHA CERTA''')   
            sleep(2)
            print('--'*20)
            print('PROXIMA FASE')
        elif jogador == 3:
            print('''MUITO BEM, ESCOLHA CERTA''')
            sleep(2)
            print('--'*20)
            print('PROXIMA FASE')
        else:
            print('ESCOLHA INVÁLIDA')
            break
    if bomba == 2:
            if jogador == 1:
                print('''MUITO BEM, ESCOLHA CERTA''')
                sleep(2)
                print('-'*20)
                print('PROXIMA FASE')
            elif jogador == 2:
                print('VOCÊ PISOU EM UMA BOMBA')
                print('3')
                sleep(1)
                print('2')
                sleep(1)
                print('1')
                sleep(1)
                print('''BOOOOOOM!!!

VOCÊ MORREU.''')
                break
            elif jogador == 3:
                print('''MUITO BEM, ESCOLHA CERTA''')
                sleep(2)
                print('--'*20)
                print('PROXIMA FASE')
            else:
                print('ESCOLHA INVÁLIDA')
                break
    if bomba == 3:
            if jogador == 1:
                print('''MUITO BEM, ESCOLHA CERTA''')
                sleep(2)
                print('--'*20)
                print('PROXIMA FASE')
                print('--'*20)
            elif jogador == 3:
                print('VOCÊ PISOU EM UMA BOMBA')
                print('3')
                sleep(1)
                print('2')
                sleep(1)
                print('1')
                sleep(1)
                print('''BOOOOOOM!!!

VOCÊ MORREU.''')
                break
            elif jogador == 2:
                print('''MUITO BEM, ESCOLHA CERTA''')
                sleep(2)
                print('--'*20)
                print('PROXIMA FASE')
            else:
                  print('ESCOLHA INVÁLIDA')
    esquerda = 1
    centro = 2  
    direira = 3
    print('--'*20)

    print('''OPÇÕES PARA CAMINHAR:
1 - ESQUERDA 
2 - PARA FRENTE
3 - DIREITA''')
    print('--'*20)
    sleep(2)
    print('AS FLORES ESTÃO MAIS IRRITADAS, TOME CUIDADO!!!')
    print('--'*20)
            
    sleep(2)
    print('''FASE 2''')

    print('--'*20)
    sleep(3)
    bomba = randint (1,3)
    jogador = int(input('''PARA QUAL DIREÇÃO VAMOS
                
DIGITE AQUI:'''))

    print('--'*20)
    if bomba == 1:
        if jogador == 1:
            print('VOCÊ PISOU EM UMA BOMBA')
            print('3')
            sleep(1)
            print('2')
            sleep(1)
            print('1')
            sleep(1)
            print('''BOOOOOOM!!!
VOCÊ MORREU.''')
            break
        elif jogador == 2:
            print('''MUITO BEM, ESCOLHA CERTA''')
            sleep(2)
            print('--'*20)
            print('PROXIMA FASE')
        elif jogador == 3:
            print('''MUITO BEM, ESCOLHA CERTA''')
            sleep(2)
            print('--'*20)
            print('PROXIMA FASE')
            print('--'*20)
        else:
            print('ESCOLHA INVÁLIDA')
            break            
    if bomba == 2:
        if jogador == 1:
            print('''MUITO BEM, ESCOLHA CERTA''')
            sleep(2)
            print('--'*20)
            print('PROXIMA FASE')
        elif jogador == 2:
            print('VOCÊ PISOU EM UMA BOMBA')
            print('3')
            sleep(1)
            print('2')
            sleep(1)
            print('1')
            sleep(1)
            print('''BOOOOOOM!!!
                                
VOCÊ MORREU.''')
            break
        elif jogador == 3:
            print('''MUITO BEM, ESCOLHA CERTA''')
            sleep(2)
            print('--'*20)
            print('PROXIMA FASE')
            print('--'*20)
        else:
            print('ESCOLHA INVÁLIDA')
            break
    if bomba == 3:                
        if jogador == 1:
            print('''MUITO BEM, ESCOLHA CERTA''')
            sleep(2)
            print('--'*20)
            print('PROXIMA FASE')
            print('--'*20)
        elif jogador == 3:
            print('VOCÊ PISOU EM UMA BOMBA')
            print('3')
            sleep(1)
            print('2')
            sleep(1)
            print('1')
            sleep(1)
            print('''BOOOOOOM!!!

VOCÊ MORREU.''')
            break
        elif jogador == 2:
            print('''MUITO BEM, ESCOLHA CERTA''')
            sleep(2)
            print('--'*20)
            print('PROXIMA FASE')
            print('--'*20)
        else:
            print('ESCOLHA INVÁLIDA')
            break
    esquerda = 1
    centro = 2
    direira = 3
    print('--'*20)
    print('''OPÇÕES PARA CAMINHAR:
1 - ESQUERDA 
2 - PARA FRENTE
3 - DIREITA''')
    print('--'*20)
    sleep(2)
    print('''CHEGAMOS NA ULTIMA FASE

TOME MUITO CUIDADO''')
    sleep(2)
    print('--'*20)

    print('''PARECE QUE TEM MUITO MAIS FLORES NO CAMINHO''')
                                
    sleep(2)
    print('--'*20)

    print('''FASE 3''')

    print('--'*20)
    sleep(2)
    jogo = True
                                
    bomba = randint (1,3)
    jogador = int(input('''PARA QUAL DIREÇÃO VAMOS
                        
DIGITE AQUI:'''))
    if bomba == 3:
        if jogador == 3:
            print('VOCÊ PISOU EM UMA BOMBA')
            print('3')
            sleep(1)
            print('2')
            sleep(1)
            print('1')
            sleep(1)
            print('''BOOOOOOM!!!
                                        
VOCÊ MORREU.''')
            break
        elif jogador == 2:
            print('''MUITO BEM, ESCOLHA CERTA''')
            sleep(2)
            print('--'*20)
            print('''PARABÉNS VOCÊ PASSOU POR TODAS AS FASES''')
            print('--'*20)
        elif jogador == 1:
            print('''MUITO BEM, ESCOLHA CERTA''')
            sleep(2)
            print('--'*20)
            print('''PARABÉNS VOCÊ PASSOU POR TODAS AS FASES''')        
            print('--'*20)
        else:
           print('ESCOLHA INVÁLIDA')
        break
    if bomba == 2:
        if jogador == 1:
            print('''MUITO BEM, ESCOLHA CERTA''')
            sleep(2)
            print('--'*20)
            print('''PARABÉNS VOCÊ PASSOU POR TODAS AS FASES''')
            print('--'*20)
        elif jogador == 2:
            print('VOCÊ PISOU EM UMA BOMBA')
            print('3')
            sleep(1)
            print('2')
            sleep(1)
            print('1')
            sleep(1)
            print('''BOOOOOOM!!!
                                        
VOCÊ MORREU.''')
            break
        elif jogador == 3:
            print('''MUITO BEM, ESCOLHA CERTA''')
            sleep(2)
            print('--'*20)
            print('''PARABÉNS VOCÊ PASSOU POR TODAS AS FASES''')
            print('--'*20)
        else:
            print('ESCOLHA INVÁLIDA')
            break
    if bomba == 1:
        if jogador == 1:
            print('VOCÊ PISOU EM UMA BOMBA')
            print('3')
            sleep(1)
            print('2')
            sleep(1)
            print('1')
            sleep(1)
            print('''BOOOOOOM!!!

VOCÊ MORREU.''')
            break
        elif jogador == 2:
            print('''MUITO BEM, ESCOLHA CERTA''')
            sleep(2)
            print('--'*20)
            print('''PARABÉNS VOCÊ PASSOU POR TODAS AS FASES''')
            print('--'*20)
        elif jogador == 3:
            print('''MUITO BEM, ESCOLHA CERTA''')
            sleep(2)
            print('--'*20)
            print('''PARABÉNS VOCÊ PASSOU POR TODAS AS FASES''')
            print('--'*20)
        else:
            print('ESCOLHA INVÁLIDA')
            print('--'*20)