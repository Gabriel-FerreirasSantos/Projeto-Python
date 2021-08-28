from time import sleep
from função import função 
from funçãoloja import funcoesloja
from função import calculadora
from funçãoSuporte import suporte
from jogos import games

menu = ('MENU')


função.linha()
print(menu.center(26))
função.linha()
print('Loja Hardware em desenvolvimento')
print('[1] Calculadora')
print('[2] Joguinhos')
print('[3] Loja Hardware')
print('[4] Suporte')
esc1 = input('')
if esc1 == '1':
    print('[1]Adição')
    print('[2]Subtração')
    print('[3]Divisão')
    print('[4]Mutiplicação')
    print('[5]Raiz quadrada')
    print('[6]Potenciação')
    esc2 = input('')
    if esc2 == '1':
        calculadora.contademais()
    elif esc2 == '2':
        calculadora.contademenos()
    elif esc2 == '3':
        calculadora.contadedividir()
    elif esc2 == '4':
        calculadora.contademutiplicação() 
    elif esc2 == '5':
        calculadora.contaderaiz()
    elif esc2 == '6':
        calculadora.contadepotenciação() 
    else:
        print('Não encontramos essa opção')    
elif esc1 == '2':  
    função.fgamesss()
    print('[1] pedra papel tesoura')
    escolha1 = input('')
    if escolha1 == '1':
        games.pedra()
    else:
        print('Não encontramos essa opção')    
elif esc1 == '3':
    print(' ')
    print('EM desenvolvimento')
    funcoesloja.inicio()
    funcoesloja.escolha0001()


elif esc1 == '4':
    função.linha2()
    suporte.opções()    