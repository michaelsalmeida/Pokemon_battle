from funcoes import *

def senha(txt = 'Digite a senha: ', txt2 = 'Senha cadastrada com sucesso'):

    especial = ['"', '!', '@', '#', '$', '%', '¨', '&', '*', '(' , ')', '_', '-', '+', '=', '{', '[', '}', ']', '?', '/', '°', ':', ';', '>', '.', '<', ',', '|']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    grande = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    while True:
        xx()
        espec = False
        num = False
        upper = False
        comp = False

        requisitos = '''
REQUISITOS PARA CRIAR A SENHA:
        
1 -> TER 7 OU MAIS CARACTÉRES
2 -> TER AO MENOS 1 LETRA MAIÚSCULA
3 -> TER AO MENOS 1 NÚMERO
4 -> TER AO MENOS 1 CARACTER ESPECIAL
        
'''

        print(requisitos)

        x = str(input(txt))


        for l in especial:
            if l in x:
                espec = True


        for a in numeros:
            if a in x:
                num = True

        for b in grande:
            if b in x:
                upper = True


        if len(x) > 7:
            comp = True


        if espec == True and num == True and upper == True and comp == True:
            y = str(input('Digite a senha novamente: '))

            if y == x:
                xx()
                print(txt2)
                z(2)
                xx()
                return x

            elif y != x:
                print('Senha diferente da digitada anterior, começe de novo.')
                z(2)
            

        else:
            print('Senha não atende aos requisitos minimos.')


def nickname(txt = 'Digite seu nick no jogo: '):
    while True:
        try:
            a = input(txt).strip()

        except:
            print('\033[31mERRO!!!! Digite seu nick novamente.')

        else:
            xx()
            cabecalhonotebook('\033[31mAtenção: Existe diferenca entre Maiúsculos e minúsculos\033[m')
            x = menuSouN(f'Seu nick será \033[32m{a}\033[m, prosseguir?')

            if x == 1:
                return a


def pegar_do_txt(arqui):
    lst = {}

    with open (arqui, 'rt') as arc:
            cont = 1
            chars = '\n'
            prod = ''
            for valor in arc:
                if cont % 2 == 0:
                    res = valor.translate(str.maketrans('', '', chars))
                    lst[prod] = res
                    cont += 1

                else:
                    res = valor.translate(str.maketrans('', '', chars))
                    prod = res
                    lst[res] = 0
                    cont += 1

    return lst


def salvar_usuarios(arqui, lst):
    with open(arqui, 'wt') as arc:
        for iten in lst:
            arc.write(f'{iten}\n')
            arc.write(f'{lst[iten]}\n')




def cadastro_novo_usuario():
    
    logins = pegar_do_txt('usuarios/logins.txt')
    
    while True:
        
        xx()
        cabecalhonotebook('Criando cadastro, preencha todos os campos corretamente.')
        login = nickname()
        if login in logins:

            xx()
            print('Esse usuário ja existe, tente outro por favor.')
            z(2)

        else:
            password = senha('Digite a senha: ', 'Usuário cadastrado com sucesso')

            dir(login)

            with open(f'saves/{login}/pokemon.txt', 'w+') as arc:
                pass

            with open(f'saves/{login}/treinador.txt', 'w+') as arc:
                pass


            logins[login] = password

            salvar_usuarios('usuarios/logins.txt', logins)

            return login



def entrar_conta():
    logins = pegar_do_txt('usuarios/logins.txt')
    
    while True:
        xx()
        usua = str(input('Digite seu nick no jogo: ')).strip()
        password = str(input('Digite sua senha: ')).strip()

        if usua not in logins or logins[usua] != password:
            print('Usuário ou senha incorretos, tente novamente.')
            z(2)

        elif usua in logins and logins[usua] == password:
            xx()
            cabecalhonotebook(f'\033[32mBem vindo de volta {usua}.\033[m')
            z(1)
            return usua



def excluir_conta():
    logins = pegar_do_txt('usuarios/logins.txt')
    
    while True:
        xx()
        usua = str(input('Digite o nick da conta que será excluida: ')).strip()
        password = str(input('Digite a senha da conta que será excluida: ')).strip()

        if usua not in logins or logins[usua] != password:
            print('Usuário ou senha incorretos, tente novamente.')
            z(2)


        elif usua in logins and logins[usua] == password:
            xx()
            s = menuSouN(f'ATENÇÃO!!!! {usua} será excluido e não será possivel recuperar a conta. PROSSEGIR MESMO ASSIM?')


            if s == 1:
                from os import remove, rmdir
                logins.pop(usua)
                remove(f'./saves/{usua}/treinador.txt')
                remove(f'./saves/{usua}/pokemon.txt')
                rmdir(f'./saves/{usua}')
                salvar_usuarios('usuarios/logins.txt', logins)

                xx()

                cabecalhonotebook('USUÁRIO EXCLUIDO COM SUCESSO.')
                z(2)

                return logins
            
            else:
                break


def salvar_informacoes(nome, nivel, vida, atk, defesa, velocidade, itens, nomepoke, pokedollar, vidaoriginal):
    with open (f'saves/{nome}/treinador.txt', 'w+') as p:
        
        for item in itens: # Loop dos itens

            # p.write(f'{item}\n') # Nome do item.
            p.write(f'{str(itens[item][0])}\n') # Quantidade do item.

        p.write(f'{pokedollar}\n')


    with open (f'saves/{nome}/pokemon.txt', 'w+') as s:
        s.write(f'{nomepoke}\n{nivel}\n{vida}\n{atk}\n{defesa}\n{velocidade}\n{vidaoriginal}')

