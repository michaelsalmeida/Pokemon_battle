def prosseguir():
    z(0.5)
    input('\n\033[32mAPERTE ENTER PARA CONTINUAR!!!!\033[m')


def xx():
    from os import system
    import platform
    a = platform.system()

    if a == 'Windows':
        system('cls')

    elif a == 'Linux':
        system('clear')



def z(tempo):
    from time import sleep
    return sleep(tempo)



def dir(name):
    import os
    os.mkdir(f'./saves/{name}')



def linha(tam = 80):
    return '-' * tam




def cabecalho(txt):
    print(linha())
    print(f'{txt:^80}')
    print(linha())

def linhanotebook(tam = 177):
    return '-' * tam

def cabecalhonotebook(txt):
    print(linhanotebook())
    print(f'{txt:^177}')
    print(linhanotebook())

def leiaint(txt):
    while True:
        try:
            a = int(input(txt))

        except:
            print('\033[31mPOR FAVOR, DIGITE UM NÚMERO VÁLIDO\033[m')

        else:
            if a < 0:
                print('Digite um valor correto.')

            else:
                return a

def menu(titulo, lst):

    cabecalho(titulo)
    for item in range (0, len(lst)):
        print(f'{item + 1} ---- {lst[item]}')

    op = [1, 2, 3, 4]
    while True:
        opcao = leiaint('Sua opção: ')

        if opcao in op:
            return opcao

        else:
            print('033[31mOPÇÃO INVÁLIDA033[m')



def menuu(titulo, lst):

    it = []
    qtd = []

    for valor in lst:  # Loop para caso a função receber um dicionário, mostrando só os índices desse dicionário.
        it.append(valor)

    cabecalho(titulo)
    for item in range (0, len(it)):
        print(f'{item + 1} ---- {it[item]}')

    while True:
        x = leiaint('SUA OPÇÃO: ')

        if x > len(it) or x < 1:
            print('\033[31mDIGITE UMA OPÇÃO VÁLIDA\033[m')
        
        else:
            return it[x - 1]

def menuu2(titulo, lst):

    it = []
    qtd = []

    for valor in lst:  # Loop para caso a função receber um dicionário, mostrando só os índices desse dicionário.
        it.append(valor)

    cabecalho(titulo)
    for item in range (0, len(it)):
        print(f'{item + 1} ---- {it[item]}')

    while True:
        x = leiaint('SUA OPÇÃO: ')

        if x > len(it) or x < 1:
            print('\033[31mDIGITE UMA OPÇÃO VÁLIDA\033[m')
        
        else:
            return x

def menudict(titulo, lst): # Menu específico para a mochila, exibindo nome do item e a quantidade que possui.
    it = []
    qtd = []
    cura = []

    for valor in lst:
        it.append(valor)
        qtd.append(lst[valor][0])
        cura.append(lst[valor][1])

    cabecalho(titulo)
    for item in range (0, len(it)):
        print(f'{item + 1} ---- {it[item]:<15}      aumenta {cura[item]:<4} de HP            possui: {qtd[item]}')

    print(f'{len(it) + 1} ---- SAIR')

    while True:
        x = leiaint('SUA OPÇÃO: ')

        if x > len(it) + 1 or x < 1:
            print('\033[31mDIGITE UMA OPÇÃO VÁLIDA\033[m')
        
        else:
            return it[x - 1]

def menudict2(titulo, lst): # Menu específico para a mochila, exibindo nome do item e a quantidade que possui.
    it = []
    qtd = []
    cura = []

    for valor in lst:
        it.append(valor)
        qtd.append(lst[valor][0])
        cura.append(lst[valor][1])

    cabecalho(titulo)
    for item in range (0, len(it)):
        print(f'{item + 1} ---- {it[item]:<15}      aumenta {cura[item]:<4} de HP            possui: {qtd[item]}')



def menuSouN(titulo, lst = ['SIM', 'NÃO']): # Menu específico para perguntas cuja as respostas serão sim ou não.

    cabecalho(titulo)
    for item in range (0, len(lst)):
        print(f'{item + 1} ---- {lst[item]}')

    while True:
        x = leiaint('SUA OPÇÃO: ')

        if x > len(lst) or x < 1:
            print('\033[31mDIGITE UMA OPÇÃO VÁLIDA\033[m')
        
        else:
            return x 



def menum(titulo, lst): # Menu específico para mostrar nome e vida dos 2 pokémons.

    cabecalho(titulo)
    a =      f'''1 - {lst[0]}                                                          2 - {lst[1]}
                                    
                                    3 - {lst[2]}'''

    print(a)

    op = [1, 2, 3]
    while True:
        opcao = leiaint('Sua opção: ')

        if opcao in op:
            return opcao

        else:
            print('033[31mOPÇÃO INVÁLIDA033[m')



def pokemonevida(pokémon1, pokémon2, vida1, vida2):
    status = f'''{pokémon1}                                                            {pokémon2}

                                    \033[31mVS\033[m

\033[32mVIDA: {vida1}\033[m                                                            \033[32mVIDA: {vida2}\033[m'''

    print(status, '\n\n')



def ataquedoturno(dono_do_turno, ataques):
    nome_ataques = []

    cabecalho(f'O que o {dono_do_turno} fará?')
    cont = 1
    for atk in ataques:
        nome_ataques.append(atk)
        print(f'{cont} - {atk:<10} -   PP {ataques[atk][2]:<10}                        ' , end = '')
        if cont == 2:
            print('\n\n')

        cont += 1

    print('\n\n')

    op = [1, 2, 3, 4]
    while True:
        opcao = leiaint('Sua opção: ')

        if opcao in op:
            return nome_ataques[opcao - 1]

    

