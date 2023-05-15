from time import sleep

print('?  '*20)
print('AGORA VAMOS TESTAR SEU RACIOCÍNIO LÓGICO.')
sleep(1)
print('HÁ CADA RESPOSTA CERTA VOCÊ GANHA 1,5 PONTOS')
print('?  '*20)
escolha = int(input('''ESTÁ PREPARADO?
1 - SIM 
2 - NÃO
DIGITE AQUI:'''))
if escolha == 1:
    print('VOCÊ VAI SE SAIR BEM NESSA ENTÃO')
elif escolha == 2:
    print('BOA SORTE ENTÃO')
else:
    print('errou')
resposta1 = 'c'
resposta2 = 'd' 
resposta3 = 'a'
resposta4 = 'c'
resposta5 = 'b'
resposta6 = 'b'
resposta7 = 'd'
resposta8 = 'a'
resposta9 = 'a'
resposta10 = 'd'
resposta11 = 'b'
resposta12 = 'd'
resposta13 = 'b'
resposta14 = 'c'
resposta15 = 'c'
jogador = 0
sleep(2)
print('?  '*20)
print('1° PERGUNTA')
print('?  '*20)
sleep(2)
pergunta1 = str(input('''O QUE SÓ AUMENTA E NUNCA DIMINUI?

A - BURACO
B - NUVEM
C - IDADE 
D - PLANTA

QUAL SUA RESPOSTA:'''))
if pergunta1 == resposta1:
    print('''MUITO BEM!
RESPOSTA CERTA.''')
else:
    print('ESCOLHA ERRADA')
sleep(2)
print('?  '*20)
print('2° PERGUNTA')
print('?  '*20)
sleep(2)
pergunta2 = str(input('''O QUE SE MOLHA ENQUANTO SECA?

A - SECADOR
B - NUVEM
C - CHUVEIRO
D - TOALHA

QUAL A SUA RESPOSTA:'''))
if pergunta2 == resposta2:
    print('''MUITO BEM!
RESPOSTA CERTA''')
    sleep(1)
    print('A TOALHA! ELA SE ENCHARCA ENQUANTO TE SECA.')
    jogador = int(jogador + 2)
else:
    print('ESCOLHA ERRADA')
sleep(2)
print('?  '*20)
print('3° PERGUNTA')
print('?  '*20)
sleep(2)
pergunta3 = str(input('''SE, DURANTE UMA CORRIDA DE CAVALOS, VOCÊ DEIXA O SEGUNDO COLOCADO PRA TRÁS, 
QUAL É A SUA COLOCAÇÃO APÓS A UNTRAPASSAGEM?

A - 2° LUGAR 
B - 1° LUGAR 
C - 5° LUGAR 
D - 3° LUGAR 

QUAL SUA RESPOSTA:'''))
if pergunta3 == resposta3:
    print('''MUITO BEM!
RESPOSTA CERTA''')
    sleep(1)
    print('SEGUNDO LUGAR ORAS, VOCÊ TOMOU O LUGAR DELE, ENTÃO VAI OCUPAR O MESMO LUGAR UAI')
    jogador = int(jogador + 2)
else:
    print('ESCOLHA ERRADA')
sleep(2)
print('?  '*20)
print('4° PERGUNTA')
print('?  '*20)
sleep(2)
pergunta4 = str(input('''A MÃE DE KAREN TEM CINCO FILHAS: DADÁ, DEDÉ, DIDÍ, DODÓ E...?

A - DUDÚ 
B - DADÃO
C - KAREN
D - RENATA

QUAL SUA RESPOSTA:  '''))
if pergunta4 == resposta4:
    print('''MUITO BEM!
RESPOSTA CERTA''')
    sleep(1)
    print('''KAREN! SE ELA É A MÃE DE KAREN E JÁ FALOU O NOME DAS OUTRAS 4 FILHAS 
ENTÃO SÓ FALTA A KAREN PARA DAR 5.''')
    jogador = int(jogador + 2)
else:
    print('ESCOLHA ERRADA')
sleep(2)
print('?  '*20)
print('5° PERGUNTA')
print('?  '*20)
sleep(2)
pergunta5 = str(input('''EM UMA SALA QUDRADA, TEMOS UMA CALOPSITA EM CADA CANTO. 
CADA CALOPSITA VÊ OUTRAS TRÊS.
QUANTAS CALOPSITAS HÁ NO TOTAL?

A - 16 
B - 4 
C - 12
D - 8 

QUAL SUA RESPOSTA:'''))
if pergunta5 == resposta5:
    print('''MUITO BEM!
RESPOSTA CERTA''')
    sleep(1)
    print('''SÓ PODE SER 4. SE A SALA É QUADRADA E HÁ UMA EM CADA CANTO, SÓ CABEM 4 MESMO.
E CADA UMA DELAS VÊ AS OUTRAS TRÊS NOS TRÊS CANTOS RESTANTES.''')
    jogador = int(jogador + 2)
else:
    print('ESCOLHA ERRADA')
sleep(2)
print('?  '*20)
print('6° PERGUNTA')
print('?  '*20)
sleep(2)
pergunta6 = str(input('''RAUL FOI SOZINHO ATÉ UMA PADARIA NO CENTRO DA CIDADE.
DURANTE O PERCURSO, ENCONTROU DOIS GAROTOS PASSEANDO COM TRÊS GATOS,
QUE ESTAVAM BRINCANDO COM DOIS PATOS, QUE, POR SUA VEZ, TINHAM DOIS DONOS.

QUANTOS SERES NO TOTAL FORAM COM RAUL ATÉ A PADARIA?

1 - 5
2 - 0
3 - 7
4 - 10

QUAL SUA RESPOSTA: '''))
if pergunta6 == resposta6:
    print('''MUITO BEM!
RESPOSTA CERTA''')
    sleep(1)
    print('''ZERO. PORQUE ELE SÓ ENCONTROU OS OUTROS NA RUA,
MAS NO TEXTO DIZ QUE ELE FOI SOZINHO ATÉ A PADARIA.''')
    jogador = int(jogador + 2)
else:
    print('ESCOLHA ERRADA')
sleep(2)
print('?  '*20)
print('7° PERGUNTA')
print('?  '*20)
sleep(2)
pergunta7 = str(input('''QUAL É O VALOR DA METADE DA METADE DO NÚMERO 20?

1 - 10
2 - 15
3 - 20
4 - 5 

QUAL SUA RESPOSTA:'''))
if pergunta7 == resposta7:
    print('''MUITO BEM!
RESPOSTA CERTA''')
    jogador = int(jogador + 2)
else:
    print('ESCOLHA ERRADA')
sleep(2)
print('?  '*20)
print('8° PERGUNTA')
print('?  '*20)
sleep(2)
pergunta8 = str(input('''O QUE PESA MAIS: UMA TONELADA DE ALGODÃO OU DE CHUMBO?

A - NENHUM
B - ALGODÃO
C - CHUMBO 

QUAL SUA RESPOSTA: '''))
if pergunta8 == resposta8:
    print('''MUITO BEM!
RESPOSTA CERTA''')
    print('NENHUM DOS DOIS PESA MAIS, ELES TÊM O MESMO PESO:UMA TONELADA')
    jogador = str(jogador + 2)
else:
    print('ESCOLHA ERRADA')
sleep(2)
print('?  '*20)
print('9° PERGUNTA')
print('?  '*20)
sleep(2)
pergunta9 = str(input('''O QUE SOBE E DESCE, MAIS SEMPRE PERMANECE NO MESMO LUGAR?

A - ESCADA
B - AVIÃO
C - ESCADA ROLANTE
D - LADEITA

QUAL A SUA RESPOSTA:'''))
if pergunta9 == resposta9:
    print('''MUITO BEM!
RESPOSTA CERTA''')
    print('A ESCADA! O QUE MAIS PODERIA SER')
    jogador = (jogador + 2)
else:
    print('ESCOLHA ERRADA')
sleep(2)
print('?  '*20)
print('10° PERGUNTA')
print('?  '*20)
sleep(2)
pergunta10 = str(input('''ALGUNS MESES TÊM 30 DIAS, OUTROS 31.
QUANTOS TEM 28 DIAS?

A - 6
B - 9
C - 1
D - TODOS

QUAL SUA RESPOSTA: '''))
if pergunta10 == resposta10:
    print('''MUITO BEM!
RESPOSTA CERTA''')
    sleep(1)
    print('''TODOS! NÃO EXISTE NENHUMM MÊS QUE NÃO CHEGUE ATÉ O DIA 28. 
FEVEREIRO PODE TER ATÉ PARAR POR AÍ, MAS TODOS TÊM NO MÍNIMO 28 DIAS.''')
    jogador = (jogador + 2)
else:
    print('ESCOLHA ERRADA')
sleep(2)
print('?  '*20)
print('11° PERGUNTA')
print('?  '*20)
sleep(2)
pergunta11 = str(input('''(VALE) ESTÁ PARA (AVLE) ASSIM COMO 5927 ESTÁ PARA...

A - 2759
B - 9527
C - 7295
D - 2597

QUAL SUA RESPOSTA:'''))
if pergunta11 == 1:
    print('''MUITO BEM!
RESPOSTA CERTA''')
    sleep(1)
    print(''' 9527. SÓ OS DOIS PRIMEIROS CARACTERES FORAM INVERTIDOS. 
POR ACASO VOCÊ INVERTEU TUDO?''')
    jogador = (jogador + 2)
else:
    print('ESCOLHA ERRADA')
sleep(2)
print('?  '*20)
print('12° PERGUNTA')
print('?  '*20)
sleep(2)
pergunta12 = str(input('''HÁ UM RATO ENTRE DOIS RATOS, UM RATO ATRÁS DE UM RATO NA FRENTE DE OUTRO RATO.
DE QUANTOS RATOS ESTAMOS FALANDO?

A - 2
B - 6
C - 9
D - 3

QUAL SUA RESPOSTA:'''))
if pergunta12 == resposta12:
    print('''MUITO BEM!
RESPOSTA CERTA''')
    sleep(1)
    print('''3 RATOS.
AFINAL, HÁ DIFERENTES FORMAS DE DESCREVER UMA MESMA CENA:

O SEGUNDO ESTÁ NO MEIO DO PRIMEIRO E DO TERCEIRO.
O TERCEIRO ESTÁ NA FRENTE DO SEGUNDO. 
E O PRIMEIRO ESTÁ ATRÁS DO SEGUNDO.''')
    jogador = (jogador + 2)
else:
    print('ESCOLHA ERRADA')
sleep(2)
print('?  '*20)
print('13° PERGUNTA')
print('?  '*20)
sleep(2)
pergunta13 = str(input('''O QUE UM FILHO DE UM MATEMÁTICO FALA QUANDO QUER IR AO BANHEIRO?

A - A MATEMÁTICA NÃO MENTE. MENTE QUEM FAZ MAU USO DELA.

B - QUERO FAZER PIPI.

C - A VIDA É TIPO MATEMÁTICA. SE TA FÁCIL, TA ERRADO.

D - ACHO QUE O MEU CUPIDO GOSTA DE MATEMÁTICA, SÓ ME TRÁS PROBLEMAS.

QUAL SUA RESPOSTA:'''))
if pergunta13 == resposta13:
    print('''MUITO BEM!
RESPOSTA CERTA''')
    jogador = (jogador + 2)
else:
    print('ESCOLHA ERRADA')
sleep(2)
print('?  '*20)
print('14° PERGUNTA')
print('?  '*20)
sleep(2)
pergunta14 = str(input('''EU ESTAVA CAMINHANDO NA PRAIA E ENCONTREI 20 PEDRAS AO LONGO DA MARGEM DIREITA.
NO REGRESSO, CONTEI 20 PEDRAS À ESQUERDA.
QUANTAS PEDRAS ESSE CAMINHO TEM NO TOTAL?

A - 20 
B - 5
C - 10
D - 40

QUAL SUA RESPOSTA:'''))
if pergunta14 == resposta14:
    print('''MUITO BEM!
RESPOSTA CERTA''')
    sleep(1)
    print('''20. TANTO NA IDA QUANTO NA VOLTA EU VI AS MESMAS PEDRAS, 
MAS POR CAUSA DO MEU SENTIDO ELAS APARECEM PRIMEIRO NA DIREITA E, DEPOIS DE EU ME VIRAR, NA ESQUERDA.''')
    jogador = (jogador + 2)
else:
    print('ESCOLHA ERRADA')
sleep(2)
print('?  '*20)
print('15° PERGUNTA')
print('?  '*20)
sleep(2)
pergunta15 = str(input('''UMA FAMÍLIA RESOLVEU IR AO SPA. ENTRARAM 1 AVÓ, 2 MÃES, 2 FILHAS E 1 NETA.
QUAL O NÚMERO MINÍMO DE MULHERES DESSA FAMÍLIA QUE ENTRARAM NESSE SPA?

A - 5
B - 6
C - 3

QUAL SUA RESPOSTA:'''))
if pergunta15 == resposta15:
    print('''MUITO BEM!
RESPOSTA CERTA''')
    sleep(1)
    print('''SÓ TRÊS MESMO. É TUDO QUESTÃO DE PONTO DE VISTA.''')
    jogador = (jogador + 2)
else:
    print('ESCOLHA ERRADA')
sleep(2)
print('CALCULANDO SUA PONTUAÇÃO')
sleep(1)
print('AGUARDE...')
sleep(3)
jogador = jogador/3
print('SUA PONTuAÇÃO ',jogador)