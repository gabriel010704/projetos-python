from random import randint 

from time import sleep

sim = 1 
nao = 2 
vamos_jogar = 2
jogar = False
while jogar == False:
    print ('========== JO KEN PO ==========')
    print ('''SUAS OPÇÕES: 
    1-SIM
    2-NÃO''')
    vamos_jogar = str(input('VAMOS JOGAR JO KEN PÔ? '))
    if vamos_jogar == 2:
        print ('OK, VOLTE OUTRA HORA. ')
        StopIteration
    elif vamos_jogar == 1:
        jogar = True
        print('ÓTIMO, VAMOS COMEÇAR')
    else:
        print('ESCOLHA INVALIDA')
itens = ('PEDRA', 'PAPEL', 'TESOURA')
maquina = randint (0, 2)
print ('~~'*14)
print ('AGORA VAMOS JOGAR JO KEN PÔ')
print ('''SUAS ESCOLHAS:
0-PEDRA
1-PAPEL
2-TESOURA''')
jogador = str(input('QUAL SUA JOGADA? '))
print ('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('~~'*14)
print ('E O VENCEDOR É ')
sleep(2)
print('~~'*14)
print('MAQUINA JOGOU {}'.format(itens,maquina))
print('JOGADOR JOGOU {}'.format(itens[jogador]))
print('~~'*14)
if maquina == 0:
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('VOCÊ VENCEU, PARABÉNS ')
    elif jogador == 2:
        print('QUE PENA, VOCÊ PERDEU ')
    else:
        print('JOGADA INVÁLIDA')
if maquina == 1:
    if jogador == 0:
        print('QUE PENA, VOCÊ PERDEU')
    elif jogador == 1:
        print('EMPATOU')
    elif jogador == 2:
        print('VOCÊ VENCEU, PARABÉNS')
    else:
        print('JOGADA INVÁLIDA')
if maquina == 2:
    if jogador == 0:
        print('VOCÊ VENCEU, PARABÉNS')
    elif jogador == 1:
        print('QUE PENA VOCÊ PERDEU')
    elif jogador == 2:
        print('EMPATOU')
        print('~~'*15)