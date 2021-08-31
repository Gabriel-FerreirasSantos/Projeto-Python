from função import função

def opções():
    print('[1] Como usar o programa')
    print('[2] Sobre o programa')
    print('[3] Erros ')
    print('[4] Feedbak')
    print('[5] Entre em contato')
    esc3 = input('').strip()
    if esc3 == '1':
        print('[1] Calculadora')
        print('[2] Jogos')
        print('[3] Suporte')
        esc4 = input('').strip()
        if esc4 == '1':
            função.linha3()
            print('máquina dotada de dispositivos mecânicos ou de programa')
            print('computacional que faz cálculos matemáticos máquina de calcular.')
        elif esc4 == '2':
            função.fgamesss()   
            print('Games para teste e aprendizado nosso')
            print('Fique a vontade para testar ver bugs e melhorias')
            print('Aceitamos feedbak sempre') 
        elif esc4 == '3':
            função.linha5()
            print('Tire suas dúvida de feedbak e conheça o programa')  
        else:
            print('Não encontramos essa opção tente novamente')      
    elif esc3 == '2':
        função.linha5()
        print('Programa Publico')
        print('Licencia Mit')
        print('0.1v')
    elif esc3 == '3':
        função.linha6()
        print('Erros bugs denuncie na area de feedbak')
    elif esc3 == '4':
        função.linha7()
        print('gabriel.conta7k@gmail.com')
        print('jaosoares76@gmail.com')
        função.ln1
    elif esc3 == '5':
        função.linha8()
        print('Entre em contatoem nosso git-Hub')
        print('João Vitor')
        print('JOAO-VITOR-SOARES') 
        print('Gabriel Ferreira Dos Santos')
        print('Gabriel-FerreirasSantos')
    else:
        print('Não encontramos essa opção')  