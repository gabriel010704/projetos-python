
from random import randint

sim = 1
nao = 2
vamos_jogar = 2

jogar = False
while jogar == False:
    print('''SUAS OPÇÕES:
  [ 1 ] SIM
  [ 2 ] NÃO''')
    vamos_jogar = int(input('VAMOS JOGAR JO KEN PÔ? '))
    if vamos_jogar == 2:
        print('OK, VOLTE OUTRA HORA')
        break
    elif vamos_jogar == 1:
        jogar = True
        print('ÓTIMO, VAMOS COMEÇAR')

    itens = ('PEDRA', 'PAPEL', 'TESOURA')
    maquina = randint(0, 2)
    print('-=' * 14)
    print ('AGORA VAMOS JOGAR JO KEN PO!!!')
    print ('''Suas opções:
  [ 0 ] PEDRA
  [ 1 ] PAPEL
  [ 2 ] TESOURA ''')
    jogador = int(input('Qual é a sua jogada? '))
    print('JO')
    print('KEN')
    print('PÔ')
    print('-=' * 14)
    print ('MÁQUINA JOGOU {}'.format(itens[maquina]))
    print('VOCÊ JOGOU {}'.format(itens[jogador]))
    print('-=' * 14)
    ganhou = False
    while ganhou == False:
        if maquina == 0:
            if jogador == 0:
                print ('EMPATOU, TENTE NOVAMENTE')
            elif jogador == 1:
                print('VOCÊ GANHOU, PARABÉNS')
            elif jogador == 2:
                print('QUE PENA VOCÊ PERDEU')
            elif maquina == 1:
                if jogador == 0:
                    print ('QUE PENA VOCÊ PERDEU')
                elif jogador == 1:
                    print('EMPATOU,TENTE NOVAMENTE')
                elif jogador == 2:
                    print ('VOCÊ GANHOU, PARABÉNS')
                elif maquina == 2:
                    if jogador == 0:
                        print('VOCÊ GANHOU, PARABÉNS')
                    elif jogador == 1:
                        print('QUE PENA VOCÊ PERDEU')
                    elif jogador == 2:
                        print('EMPATOU, TENTE NOVAMENTE')
                        print('-=' * 14)
                    ganhou = True

