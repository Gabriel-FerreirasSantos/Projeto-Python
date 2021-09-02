from função import função


def opções():
    print('[1] Como usar o programa')
    print('[2] Sobre o programa')
    print('[3] Erros ')
    print('[4] Feedbak')
    print('[5] Entre em contato')
    função.linha()
    esc3 = input('R:').strip()
    if esc3 == '1':
        função.linha()
        print('[1] Calculadora')
        print('[2] Jogos')
        print('[3] Suporte')
        função.linha()
        esc4 = input('R:').strip()
        if esc4 == '1':
            função.linha3()
            print('máquina dotada de dispositivos mecânicos ou de programa')
            print('computacional que faz cálculos matemáticos máquina de calcular.')
            função.linha()
        elif esc4 == '2':
            função.fgamesss()   
            print('Games para teste e aprendizado nosso')
            print('Fique a vontade para testar ver bugs e melhorias')
            print('Aceitamos feedbak sempre') 
            função.linha()
        elif esc4 == '3':
            função.linha5()
            print('Tire suas dúvida de feedbak e conheça o programa') 
            função.linha() 
        else:
            print('Não encontramos essa opção tente novamente')
            função.linha()
    elif esc3 == '2':
        função.linha5()
        print('Programa Publico')
        print('Licencia Mit')
        print('0.1v')
        função.linha()
    elif esc3 == '3':
        função.linha6()
        print('Erros bugs denuncie na area de feedbak')
        função.linha()
    elif esc3 == '4':
        função.linha7()
        print('Entre em contato com')
        print('contato.programerflix@gmail.com')
        função.linha()
    elif esc3 == '5':
        função.linha8()
        print('Entre em contato em nosso GitHub')
        print('Gabriel Ferreira Dos Santos')
        print('Gabriel-FerreirasSantos')
        print('contato.programerflix@gmail.com')
        função.linha()
    else:
        print('Não encontramos essa opção')  