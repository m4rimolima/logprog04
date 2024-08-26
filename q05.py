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
            a-Soma
            b-Subtração
            c-Multiplicação
            d-Divisão
            e-Elevar ao quadrado
            ''')
        
        ope = input ('Escolha uma operação: ')
        if ope == 'a':
            print('Escolheu a soma')
            n1= int(input('diga-me um número: '))
            n2= int(input('diga-me outro número: '))
            print(f'{n1+n2}')

        if ope == 'b':
            print('Escolheu a subtração')
            n1= int(input('diga-me um número: '))
            n2= int(input('diga-me outro número: '))
            print(f'{n1-n2}')

        if ope == 'c':
            print('Escolheu a multiplicação')
            n1= int(input('diga-me um número: '))
            n2= int(input('diga-me outro número: '))
            print(f'{n1*n2}')

        if ope == 'd':
            print('Escolheu a divisão')
            n1= int(input('diga-me um número: '))
            n2= int(input('diga-me outro número: '))
            print(f'{n1/n2}')

        if ope == 'e':
            print('Escolheu elevar o número ao quadrado')
            n1= int(input('diga-me um número: '))
            print(f'{n1*n1}')

