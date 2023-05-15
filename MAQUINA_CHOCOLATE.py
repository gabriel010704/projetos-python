from time import sleep

print('+-+'*14) 
print('BEM VINDO A NOSSA MAQUINA DE CHOCOLATE')
print('+-+'*14)
sleep(2)

opcao = False
while opcao == False:
    usuario = int (input('''QUAL CHOCOLATE VOCÊ IRÁ SABOREAR?

1 - TIPO A  80% CACAU
2 - TIPO B  85% CACAU
3 - TIPO C  90% CACAU

DIGITE AQUI: '''))
    print('+-+'*14)
    print('AGUARDE...')
    print('+-+'*14)
    sleep(5)
    if usuario == 1:
        print('PREPARANDO CHOCOLATE TIPO A 80% CACAU')
        print('+-+'*14)
        sleep(3)
        print('''CHOCOLATE TIPO A 80% CACAU PRONTO

RETIRE LOGO ABAIXO''')
        break
    elif usuario == 2:
        print('PREPARANDO CHOCOLATE TIPO B 85% CACAU')
        sleep(3)
        print('+-+'*14)
        print('''CHOCOLATE TIPO B PRONTO

RETIRE LOGO ABAIXO''')
        break
    elif usuario == 3:
        print('PREPARANDO CHOCOLATE TIPO C 90% CACAU')
        sleep(3)
        print('+-+'*14)
        print('''CHOCOLATE TIPO C 90% CACAU PRONTO

RETIRE LOGO ABAIXO''')
        opcao == True