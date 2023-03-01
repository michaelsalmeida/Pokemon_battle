from funcoes import *
from conexao import *

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
    con = conex()

    if con != False:
        cursor = con.cursor()
        while True:
            xx()
            cabecalhonotebook('Criando cadastro, preencha todos os campos corretamente.')
            login = nickname()
            possui = "SELECT pk_login FROM login ORDER BY pk_login desc LIMIT 1;"
            cursor.execute(possui) #executa o comando.
            identt = cursor.fetchone() 

            if identt == None:
                password = senha('Digite a senha: ', 'Usuário cadastrado com sucesso')

                valores = ('default', login, password)
                comando2 = "INSERT INTO login VALUES (%s, %s, %s)"
                cursor.execute(comando2, valores)
                con.commit()

                return login

            else:
                comando1 = "SELECT nick FROM login"
                cursor.execute(comando1) #executa o comando.
                ident = cursor.fetchone() #criar uma lista com todos os nicks que estáo no banco de dados.

                existe = False
                

                for n in ident: # loop para saber se o nick ja existe no banco de dados.
                    if login == n:
                        existe = True

                if existe == True:
                    xx()
                    print('Usuário ja existe, por favor, crie um outro nick.')
                    z(3)

                else:
                    password = senha('Digite a senha: ', 'Usuário cadastrado com sucesso')

                    valores = ('default', login, password)
                    comando2 = "INSERT INTO login VALUES (%s, %s, %s)"
                    cursor.execute(comando2, valores)
                    results = cursor.fetchall()
                    con.commit()
                
                return login

    else:
        import sys
        print('Reinicie o programa.')
        sys.exit()

            

def entrar_conta():
    con = conex() #cria a conexão

    if con:

        while True:
            xx()
            cursor = con.cursor()
            usua = str(input('Digite o nick da sua conta: ')).strip()

            comando1 = 'SELECT nick FROM login'
            cursor.execute(comando1)
            lista = cursor.fetchall() #cria uma lista com todos os nicks salvos no banco de dados
            esta = False

            for usu in range (0, len(lista)): # loop para veerificar se o usuario digitado existe no banco de dados
                if usua == lista[usu][0]:
                    esta = True

            if esta:
                password = str(input('Digite a senha da sua conta: ')).strip()
                comando2 = 'SELECT pk_login FROM login WHERE nick = %s'
                cursor.execute(comando2, (usua,))
                id = cursor.fetchone() #pega o id do nick digitado que está no banco de dados
                
                comando3 = 'select senha from login where pk_login = %s'
                cursor.execute(comando3, (id[0],))
                asenha = cursor.fetchone() #pega a senha desse nick que foi digitado

                if password == asenha[0]:
                    xx()
                    dados = [usua, id[0]]

                    return dados




                else:
                        xx()
                        print('Senha inválida')

                        z(1)

                        a = menuSouN('Deseja tentar de novo?')

                        if a == 2:
                            break
                



            else:
                xx()
                print('Usuário não existe no sistema')
                z(2)
                a = menuSouN('Deseja tentar de novo?')

                if a == 2:
                    break
            


def excluir_conta():
    con = conex() #cria a conexão

    if con:

        while True:
            xx()
            cursor = con.cursor()
            usua = str(input('Digite o nick da conta que será excluida: ')).strip()

            comando1 = 'SELECT nick FROM login'
            cursor.execute(comando1)
            lista = cursor.fetchall() #cria uma lista com todos os nicks salvos no banco de dados
            esta = False

            for usu in range (0, len(lista)): # loop para veerificar se o usuario digitado existe no banco de dados
                if usua == lista[usu][0]:
                    esta = True

            if esta:
                password = str(input('Digite a senha da conta que será excluida: ')).strip()
                comando2 = 'SELECT pk_login FROM login WHERE nick = %s'
                cursor.execute(comando2, (usua,))
                id = cursor.fetchone() #pega o id do nick digitado que está no banco de dados
                
                comando3 = 'select senha from login where pk_login = %s'
                cursor.execute(comando3, (id[0],))
                asenha = cursor.fetchone() #pega a senha desse nick que foi digitado

                if password == asenha[0]:
                    xx()
                    x = menuSouN(f'Deseja realmente apagar {usua}? Essa ação não pode ser desfeita.')
                    
                    if x == 1:
                        comando4 = 'Delete from login where pk_login = %s'
                        comando5 = 'Delete from treinador where fk_login = %s'
                        comando6 = 'Delete from pokemon where fk_treinador = %s'

                        cursor.execute(comando6, (id[0], )) # teve que realizar o comando ao contrario porque nao pode apagar uma tabela principal que possui outras que dependem dela.
                        cursor.execute(comando5, (id[0], ))
                        cursor.execute(comando4, (id[0], ))

                        con.commit()
                        cursor.close()
                        con.close()

                        xx()
                        cabecalhonotebook(f'Conta {usua} excluida com sucesso.')
                        z(2)
                        break



                else:
                    xx()
                    print('Senha inválida')

                    z(1)

                    a = menuSouN('Deseja tentar de novo?')

                    if a == 2:
                        break
                



            else:
                xx()
                print('Usuário não existe no sistema')
                z(2)
                a = menuSouN('Deseja tentar de novo?')

                if a == 2:
                    break
            

        


def salvar_informacoes(nome, nivel, vida, atk, defesa, velocidade, itens, nomepoke, pokedollar, vidaoriginal):

    # essa função salva os dados no banco quando uma conta é criada.

    con = conex()

    if con:        
            cursor = con.cursor()
            possui = "SELECT pk_login FROM login ORDER BY pk_login desc LIMIT 1;"
            cursor.execute(possui) #executa o comando.
            ident = cursor.fetchone() 
            idd = ident[0]

            valores = ('default', idd, itens['potion'][0], itens['superpotion'][0], itens['hyperpotion'][0], itens['maxpotion'][0], pokedollar)
            comando = "INSERT INTO treinador VALUES (%s, %s, %s, %s, %s, %s, %s);"

            cursor.execute(comando, valores)
            con.commit()

            comando2 = "SELECT pk_treinador FROM treinador ORDER BY pk_treinador desc LIMIT 1;"
            cursor.execute(comando2) #executa o comando.
            ident = cursor.fetchone() #cria uma lista com os valores que eu quis pegar que no caso é o primeiro id.

            iddd = ident[0]

            valores2 = ('default', iddd, nomepoke, nivel, vida, atk, defesa, velocidade, vidaoriginal)
            comando3 = "INSERT INTO pokemon VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"

            cursor.execute(comando3, valores2)
            con.commit()

            cursor.close()
            con.close()

            


def salvar_informacoess(id, nivel, vida, atk, defesa, velocidade, itens, nomepoke, pokedollar, vidaoriginal):
    # essa função salva os dados no banco quando o jogo finaliza.

    con = conex()

    if con:        
            cursor = con.cursor()
            possui = "update treinador set potion = %s, superpotion = %s, hyperpotion = %s, maxpotion = %s, pokedolar = %s where pk_treinador = %s"
            valores = (itens['potion'][0], itens['superpotion'][0], itens['hyperpotion'][0], itens['maxpotion'][0], pokedollar, id)
            cursor.execute(possui, valores) #executa o comando.
            con.commit()

            comando2 = "update pokemon set nivel = %s, vida = %s, atk = %s, def = %s, velocidade = %s where pk_pokemon = %s"
            valores2 = (nivel, vida, atk, defesa, velocidade, id)
            cursor.execute(comando2, valores2) #executa o comando.
            con.commit()

            cursor.close()
            con.close()

    # with open (f'saves/{nome}/treinador.txt', 'w+') as p:
            
        #     for item in itens: # Loop dos itens

        #         # p.write(f'{item}\n') # Nome do item.
        #         p.write(f'{str(itens[item][0])}\n') # Quantidade do item.

        #     p.write(f'{pokedollar}\n')



        

# import mysql.connector

# mydb = mysql.connector.connect(

# host = "localhost",
# user = "root",
# password = "",
# database = "gamepoke"

# )

# if mydb.is_connected():
#     cursor = mydb.cursor()

#     comando2 = "SELECT id FROM treinador ORDER BY id desc LIMIT 1;"
#     cursor.execute(comando2)
#     ident = cursor.fetchone()

#     print(ident)



# con = conex()

# if con:        
#         cursor = con.cursor()
#         comando = 'select * from pokemon where pk_pokemon = %s'
#         id = 3
#         cursor.execute(comando, (id,))
#         lista = cursor.fetchall()
#         print(lista)

