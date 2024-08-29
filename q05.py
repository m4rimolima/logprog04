resp = 1
while resp != '0' :
    print ('''
        isso é uma caculadora
        deseija continuar?
        1- sim
        0- nao
        ''')
    resp = input('Resposta:')
    if resp == '1':
        print ('''
            ------calc.py------
            1-Soma
            2-Subtração
            3-Multiplicação
            4-Divisão
            5-Elevar ao quadrado
            6-Sair
            ''')
        
        ope = input ('Escolha uma operação: ')

        if ope == '1':
            print('Escolheu a soma')
            n1= int(input('diga-me um número: '))
            n2= int(input('diga-me outro número: '))
            print(f'{n1+n2}')
        else:
            if ope == '2':
                print('Escolheu a subtração')
                n1= int(input('diga-me um número: '))
                n2= int(input('diga-me outro número: '))
                print(f'{n1-n2}')
            else:
                if ope == '3':
                    print('Escolheu a multiplicação')
                    n1= int(input('diga-me um número: '))
                    n2= int(input('diga-me outro número: '))
                    print(f'{n1*n2}')
                else:
                    if ope == '4':
                        print('Escolheu a divisão')
                        n1= int(input('diga-me um número: '))
                        n2= int(input('diga-me outro número: '))
                        print(f'{n1/n2}')
                    else:
                        if ope == '5':
                            print('Escolheu elevar o número ao quadrado')
                            n1= int(input('diga-me um número: '))
                            print(f'{n1*n1}')
                        else:
                            if ope == "6":
                                print('tchau')
                            else:
                                print('erro, tente novamente')