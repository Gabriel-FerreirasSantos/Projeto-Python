from time import sleep
from função import função 
from função import calculadora
from funçãoSuporte import suporte
from jogos import games

menu = ('MENU')


função.linha()
print(menu.center(26))
função.linha()
print('Em Contrução...')
print('[1] Calculadora')
print('[2] Joguinhos')
print('[3] Suporte')
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
elif esc1 == '2':  
    função.fgamesss()
    print('Em Contrução...')
    print('[1] pedra papel tesoura')
    print('[2] ')
    escolha1 = input('')
    if escolha1 == '1':
        games.pedra()
    elif escolha1 == '2':
        print('em construção...')
        sleep(1)
elif esc1 == '3':
    função.linha2()
    suporte.opções()    