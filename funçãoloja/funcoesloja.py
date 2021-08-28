from time import sleep
#listas
lista = ['itens','Itens','Intens','intens']
listt = ['pc','PC','Pc','pC','PCS','pcs','Pcs','pCs','pCS','PcS']
llist = ['exit','sair','Sair','Exit','Exite','exite','sai','Sai' ]
memoria_ram = ['Memoria ram','memoria ram','Memória ram','memória ram','Memoriaram','memoriaram','ram','Ram','RAM']
placa_mae = ['Placa mãe','Placa mae','placa mãe','placa mae']
HD = ['HD','hD','Hd','hd']
SSD = ['SSD','Ssd','ssd','sSd','SsD','sSD']
processador = ['Processador','processador','Processado','processado']
placa_de_video = ['Placa de video','placa de video','Placa De Video',]
sim = ['SIM','Sim','sim','S','s' '']
nao = ['Não','Nao','não','nao','N','n']
cartão = ['Cartão','Cartao','cartão','cartao']
avista = ['Avista','avista']

def inicio():   
    print('----------------------------------------------')
    print('|      BEM VINDO A LOJA DE HARDWARE          |')
    print('|      AQUI VOCÊ ENCONTRA OS MELHORES        |')
    print('|          PRODUTOS COM DESCONTOS            |')
    print('----------------------------------------------')
    print('')  
    print('Para ver nossos itens digite itens.')
    print('para ver nossos computadores completo digite pc.')
    print('para sair digite sair ou exit.')

def escolha0001():
    perg = str(input(''))
    while True:
        if perg in lista: 
            print('----------------------------------------------')
            print('|                Placa mae                   |')
            print('|                HD                          |')
            print('|                SSD                         |')
            print('|                Memoria ram                 |')
            print('|                Placa de video              |')
            print('|                Processador                 |')
            print('----------------------------------------------')
            prdt = str(input('Qual produto você deseja?  '))
            if prdt in placa_mae:
                print(' ')
                print('Infelizmente estamos sem estoques de placa mãe no momento :(')
                esclh = input('Quer voltar no inicio? [sim/nao] ')
                if esclh in sim:
                    print('')
                else:
                    break    
            elif prdt in HD:
                print(' ')
                print('Temos os seguintes HD') 
                print('------------------------------------------------------------------------')
                print('|                               HD                                     |')
                print('|            Escreva apenas o Numero para para saber do intem          |')
                print('------------------------------------------------------------------------')
                print('|[1]  Disco rígido externo Seagate Expansio STEA4000400 : 4TB          |')
                print('|[2]  Disco rígido externo Seagate Expansion STEA2000400 : 2TB         |')
                print('|[3]  Disco rígido interno Western Digital WD AV-SP WD5000AVDS : 500GB |')
                print('|[4]  Disco rígido interno Western Digital WD Purple WD60PURZ : 6TB    |')
                print('------------------------------------------------------------------------')
                hd1 = input('Qual produto o Sr(a) deseja?  ') 
                if hd1 == '1':
                    print('')
                    sleep(1)
                    print('As configurações deles são as seguintes: ')
                    print('Preço: R$689')
                    print(' em 12x R$65')
                    print('---------------------------------------------------------------------------')
                    print('| É útil para salvar programas e documentos com a sua capacidade de 4 TB. |')
                    print('| tamanho de 2.5.                                                         |')
                    print('| É compatível com Windows.                                               |')
                    print('| Fácil de transportar                                                    |')
                    print('| Interface de conexão: USB 3.0                                           |')
                    print('| Adequado para PC e Notebook                                             |')
                    print('| Acessórios incluídos: cabo usb                                          |')
                    print('---------------------------------------------------------------------------')
                    comprahd1 = input('Como você quer fazer esta compra?(cartão)(Avista) ')
                    if comprahd1 in cartão:
                        print('Vamos la aqui você vai compra no cartão ')
                        print('Iremos pedir alguns dados do senhor')
                        sleep(0.4)
                        cpf = input('Qual o seu CPF? ')
                        data = input('Sua data de nascimento? ')
                        nome = input('Nome completo ')
                        cartao = input('Qual o banco do seu cartão? ')
                        ncartao = input('Qual o numero do cartao? ')
                        print('Analisando..')
                        sleep(1)
                        print('Pronto compra efetuada')
                        cidade = input('Você é de onde? ')
                        entrega = input('Entregaremos o seu HD em menos de 15 dias ')
                        voltar = input('Quer voltar no inicio? sim/nao ')
                        if voltar in sim:
                            print('')
                        else:
                            break       
                    elif comprahd1 in avista:
                        print('Vamos la aqui voce vai comprar avista')
                        print('Avista ele custa R$689')
                        print('Você ira pagar R$689')
                        sleep(0.4)
                        print('Obrigado')
                        print('Você deseja levar ou quer que nois levamos até sua casa')
                        levar = input('(se quer levar digite 1/ se quer que nois levamos digite 2) ')
                        if levar == '1':
                            print('Obrigado pela preferencia se precisar de mais itens é so nos visitar')
                            voltar = input('Quer voltar no inicio? sim/nao ')
                            if voltar in sim:
                                print('')
                            else:
                                break  
                        else:    
                            cidade = input('Você é de onde? ')
                            print('Entregaremos o seu HD em menos de 24hr ')
                            voltar = input('Quer voltar no inicio? sim/nao ')
                            if voltar in sim:
                                print('')
                            else:
                                break
                            voltar = input('Quer voltar no inicio? sim/nao ')
                            if voltar in sim:
                                print('')
                            else:
                                break
                            print('Não encontramos essa palavra {} verifique se escreveu direito e tente novamente'.format(comprahd1)) 
                            voltar = input('Quer voltar no inicio? sim/nao ')
                            if voltar in sim:
                                print('')
                            else:
                                break  
                    else:
                        print('Não encontramos essa palavra {} verifique se escreveu direito e tente novamente'.format(comprahd1)) 
                        voltar = input('Quer voltar no inicio? sim/nao ')
                        if voltar in sim:
                            print('')
                        else:
                            break           
                elif hd1 == '2':
                    print('As configurações deles são as seguintes: ')
                    print('Preço: R$452.50')
                    print(' em 12x R$42')
                    print('---------------------------------------------------------------------------')
                    print('| É útil para salvar programas e documentos com a sua capacidade de 2 TB. |')
                    print('| tamanho de 2.5.                                                         |')
                    print('| É compatível com Windows.                                               |')
                    print('| Fácil de transportar                                                    |')
                    print('| Interface de conexão: USB 3.0                                           |')
                    print('| Adequado para PC e Notebook                                             |')
                    print('| Acessórios incluídos: cabo usb                                          |')
                    print('---------------------------------------------------------------------------')
                    hd2 = input('O senhor deseja continuar a compra? [S/N] ')         
                    if hd2 in sim:
                        comprahdd2 = input('Como você quer fazer esta compra?(cartão)(Avista) ')
                        if comprahdd2 in cartão:
                            print('Vamos la aqui você vai compra no cartão ')
                            print('Iremos pedir alguns dados do senhor')
                            sleep(0.4)
                            cpf = input('Qual o seu CPF? ')
                            data = input('Sua data de nascimento? ')
                            nome = input('Nome completo ')
                            cartao = input('Qual o banco do seu cartão? ')
                            continuar = input('Deseja continuar? [S/N] ')
                            if continuar in sim:
                                ncrt = input('Qual o numero do cartao? ')
                                print('Analisando..')
                                sleep(1)
                                print('Pronto compra efetuada')
                                cidade = input('Você é de onde? ')
                                entrega = input('Entregaremos o seu HD em menos de 15 dias ')
                                entrega = input('Quer voltar no inicio? sim/nao ')
                                if entrega in sim:
                                    print('')
                                else:
                                    break  
                            elif continuar in nao:
                                voltar = input('Quer voltar no inicio? sim/nao ')
                                if voltar in sim:
                                    print('')
                                else:
                                    break
                            else:
                                print('Não encontramos essa palavra {} verifique se escreveu direito e tente novamente'.format(continuar))
                                voltar = input('Quer voltar no inicio? sim/nao ')
                                if voltar in sim:
                                    print('')
                                else:
                                    break  
                        elif comprahdd2 in avista:
                            print('Vamos la aqui voce vai comprar avista ')
                            print('Avista ele custa R$452.50')
                            print('Deseja continuar? ')
                            continuar =input('')
                            sleep(1)
                            if continuar in sim:
                                ncret = input('Vamos continuar então ')
                                print('Você ira pagar R$452.50')
                                print('Obrigado')
                                print('Você deseja levar ou quer que nois levamos até sua casa') 
                                voltar = input('(se quer levar digite 1/ se quer que nois levamos digite 2) ')
                                if voltar == '1':
                                    print('Obrigado pela preferencia se precisar de mais itens é so nos visitar')
                                    voltar = input('Quer voltar no inicio? sim/nao ')
                                    if voltar in sim:
                                        print('')
                                    else:
                                        break
                                else:    
                                    cidade = input('Você é de onde? ')
                                    print('Entregaremos o seu HD em menos de 24hr ')
                                    voltar = input('Quer voltar no inicio? sim/nao ')
                                    if voltar in sim:
                                        print('')
                                    else:
                                        break
                            elif continuar in nao:
                                volta = input('Quer voltar no inicio? sim/nao ')
                                if volta in sim:
                                    print('')
                                else:
                                    break
                            else:
                                print('Não encontramos essa palavra {} verifique se escreveu direito e tente novamente'.format(continuar))   
                                voltar = input('Quer voltar no inicio? sim/nao ')
                                if voltar in sim:
                                    print('')
                                else:
                                    break
                        else:
                            print('Não encontramos essa palavra {} verifique se escreveu direito e tente novamente'.format(comprahdd2))   
                            voltar = input('Quer voltar no inicio? sim/nao ')
                            if voltar in sim:
                                print('')
                            else:
                                break        
                    elif hd2 in nao:
                        print('Se quiser dar uma olhada nos outros itens fique avontade')
                        voltar = input('Quer voltar no inicio? sim/nao ')
                        if voltar in sim:
                            print('')
                        else:
                            break
                    else:
                        print('Não econtramos essa plavra {} verifique novamente e tente'.format(hd2))
                        voltar = input('Quer voltar no inicio? sim/nao ')
                        if voltar in sim:
                            print('')
                        else:
                            break     
                elif hd1 == '3':
                    print('As configurações deles são as seguintes: ')
                    print('Preço: R$145')
                    print(' em 12x R$13')
                    print('---------------------------------------------------------------------------')
                    print('| É útil para salvar programas e documentos com a sua capacidade de 500 GB|')
                    print('| tamanho de 3.5.                                                         |')
                    print('| É compatível com Windows e MacOS.                                       |')
                    print('| Interface de conexão: SATA II                                           |')
                    print('| Adequado para pc sistema de vdgame, DRV e receptor de tv                |')
                    print('| Aumenta o desempenho do seu computador                                  |')
                    print('---------------------------------------------------------------------------')
                    hd3 = input('O senhor deseja continuar a compra? [S/N] ')
                    if hd3 in sim:
                        hdd3 = input('Como você quer fazer esta compra?(cartão)(Avista) ')
                        if hdd3 in cartão:
                            print('Vamos la aqui você vai compra no cartão ')
                            print('Iremos pedir alguns dados do senhor')
                            sleep(0.4)
                            cpf = input('Qual o seu CPF? ')
                            data = input('Sua data de nascimento? ')
                            nome = input('Nome completo ')
                            cartao = input('Qual o banco do seu cartão? ')
                            continuar = input('Deseja continuar? [S/N] ')
                            if continuar in sim:
                                ncrt = input('Qual o numero do cartao? ')
                                print('Analisando..')
                                sleep(1)
                                print('Pronto compra efetuada')
                                cidade = input('Você é de onde? ')
                                entrega = input('Entregaremos o seu HD em menos de 15 dias ')
                                voltar = input('Quer voltar no inicio? sim/nao ')
                                if voltar in sim:
                                    print('')
                                else:
                                    break
                            elif continuar in nao:
                                voltar = input('Quer voltar no inicio? sim/nao ')
                                if voltar in sim:
                                    print('')
                                else:
                                    break
                            else:
                                print('Não encontramos essa palavra {} verifique se escreveu direito e tente novamente'.format(continuar))
                                voltar = input('Quer voltar no inicio? sim/nao ')
                                if voltar in sim:
                                    print('')
                                else:
                                    break    
                        elif hdd3 in avista:
                            print('Vamos la aqui voce vai comprar avista ')
                            print('Avista ele custa R$145')
                            print('Deseja continuar? ')
                            continua =input('')
                            sleep(1)
                            if continua in sim:
                                ncrt = input('Vamos continuar então ')
                                print('Você ira pagar R$145')
                                print('Obrigado')
                                print('Você deseja levar ou quer que nois levamos até sua casa') 
                                levar = input(' (se quer levar digite 1/ se quer q nois levamos digite 2) ')
                                if levar == '1':
                                    print('Obrigado pela preferencia se precisar de mais itens é so nos visitar')
                                    voltar = input('Quer voltar no inicio? sim/nao ')
                                    if voltar in sim:
                                        print('')
                                    else:
                                        break   
                                else:    
                                    cidade = input('Você é de onde? ')
                                    print('Entregaremos o seu HD em menos de 24hr ')
                                    voltar = input('Quer voltar no inicio? sim/nao ')
                                    if voltar in sim:
                                        print('')
                                    else:
                                        break
                            elif continua in nao:
                                voltar = input('Quer voltar no inicio? sim/nao ')
                                if voltar in sim:
                                    print('')
                                else:
                                    break
                            else:
                                print('Não encontramos essa palavra {} verifique se escreveu direito e tente novamente'.format(continua))   
                                voltar = input('Quer voltar no inicio? sim/nao ')
                                if voltar in sim:
                                    print('')
                                else:
                                    break
                    elif hd3 in nao:
                        print('Se quiser dar uma olhada nos outros itens fique avontade')
                        voltar = input('Quer voltar no inicio? sim/nao ')
                        if voltar in sim:
                            print('')
                        else:
                            break
                    else:
                        print('Não econtramos essa plavra {} verifique novamente e tente'.format(hdd3))
                        voltar = input('Quer voltar no inicio? sim/nao ')
                        if voltar in sim:
                            print('')
                        else:
                            break            
        elif perg in listt:
            print('Bem Vindo a area de pc aqui você encontra os pc completo com desconto de até 15%') 
            print('Em desenvolvimento...')
            voltar = input('')
            break
            #sad = input('O Senhor(a) deseja dar uma olhada? (sim/não)')
            #if sad in sim:
                #print('Desculpe estamos sem estoque no momento')
            #elif sad in nao:
                #print('Reinicie o programa se estiver em interesse em montar um computador')
                #print('Se não quiser obrigado por visitar a loja volte sempre quando quiser') 
                #hiasd = input('Enter')   
        elif perg in llist:
            print('Obrigado por visitar, volte quando quiser')   
            voltar = input('') 
            break                                
        else:
            print('Você não escreveu direito não encontramos essa palavra \{}/ reinicie e digite da maneira certa'.format(perg))
            voltar = input('')   
            break                     
