from time import sleep
from função import função 
from funçãoloja import funcoesloja
from função import calculadora
from funçãoSuporte import suporte
from jogos import games

menu = 'MENU'

função.linha()
print(menu.center(26))
função.linha()
print(f'Loja Hardware em desenvolvimento  V0.1')
print(f' ')
print(f'[1] Calculadora')
print(f'[2] Joguinhos')
print(f'[3] Loja Hardware')
print(f'[4] Suporte')
função.linha()
esc1 = input('')
função.linha()
if esc1 == '1':
    calc = 'Calculadora'
    print(calc.center(26))
    função.linha()
    print(f'[1]Adição')
    print(f'[2]Subtração')
    print(f'[3]Divisão')
    print(f'[4]Mutiplicação')
    print(f'[5]Raiz quadrada')
    print(f'[6]Potenciação')
    função.linha()
    esc2 = input('')
    função.linha()
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
        print(f'Não encontramos essa opção')    
elif esc1 == '2':  
    função.fgamesss()
    print(f'[1] pedra papel tesoura')
    escolha1 = input('')
    if escolha1 == '1':
        games.pedra()
    else:
        print(f'Não encontramos essa opção')
elif esc1 == '3':
    print(' ')
    print(f'Em desenvolvimento')
    funcoesloja.inicio()
    funcoesloja.escolha0001()


elif esc1 == '4':
    
    sup = 'Suporte'
    print(sup.center(26))
    função.linha()
    suporte.opções()   

else:
    print(f'Não encontramos esse numero na lista')     