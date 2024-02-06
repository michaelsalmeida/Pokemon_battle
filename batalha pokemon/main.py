from pokemon import *
from funcoes import *
from conta import *
from treinador import *
import sys


for player in range (0, 2): # Loop responsável por realizar o login dos treinadores.
    while True:
        xx()
        escolha = menu(f'Bem vindo ao POKÉPython, Treinador {player + 1}', ['ENTRAR', 'CRIAR CONTA','EXCLUIR CONTA', 'CONVIDADO', 'SAIR'])
        
        if escolha == 1:


            if player == 0:

                playerr1 = entrar_conta()
                

                coisaspokemon1 = coisaspoke(playerr1[1]) # nome, nivel, vida, atk, defesa, velocidade, vida original.
                coisastreinador1 = coisastreina(playerr1[1]) # potion, superpotion, hyperpotion, maxpotion

                        
                nome1 = playerr1[0].strip().capitalize()

                xx()

                escolhapokemon1 = coisaspokemon1[0]

                poke1 = Pokemon(escolhapokemon1, int(coisaspokemon1[1]))

                poke1.atualizar_status(coisaspokemon1)


                treinador1 = Treinador(poke1.vida, poke1.vidaorigial, poke1.ataques, nome1)

                treinador1.atualizar_itens(coisastreinador1)

                break

            else:

                playerr2 = entrar_conta()

                coisaspokemon2 = coisaspoke(playerr2[1])# nome, nivel, vida, atk, defesa, velocidade, vida original .
                coisastreinador2 = coisastreina(playerr2[1]) # potion, superpotion, hyperpotion, maxpotion.

                nome2 = playerr2[0].strip().capitalize()

                xx()

                escolhapokemon2 = coisaspokemon2[0]

                poke2 = Pokemon(escolhapokemon2, int(coisaspokemon2[1]))

                poke2.atualizar_status(coisaspokemon2)

                treinador2 = Treinador(poke2.vida, poke2.vidaorigial, poke2.ataques, nome2)

                treinador2.atualizar_itens(coisastreinador2)

                break

        
        elif escolha == 2:

            playerr3 = cadastro_novo_usuario()

            nome1 = playerr3.strip().capitalize()

            xx()

            escolhapokemon1 = menuu(f'{nome1}, escolha um pokémon para sua jornada: ', lista_pokemons())

            poke1 = Pokemon(escolhapokemon1, 35)

            treinador1 = Treinador(poke1.vida, poke1.vida, poke1.ataques, nome1)

            salvar_informacoes(playerr3, poke1.nivel, poke1.vida, poke1.atk, poke1.defesa, poke1.velocidade, treinador1.itens, escolhapokemon1, treinador1.pokedollar, poke1.vida)
        
        
        elif escolha == 3:
            playerr4 = excluir_conta()


        elif escolha == 4:
            xx()
            print(f'Treinador {player + 1}, Entrando como convidado...')
            z(2)

            if player == 0:
                nome1 = str(input('Digite o nome do treinador 1: ')).strip().capitalize()

                xx()

                escolhapokemon1 = menuu(f'{nome1}, escolha um pokémon para usar na batalha: ', lista_pokemons())

                poke1 = Pokemon(escolhapokemon1, 35)

                treinador1 = Treinador(poke1.vida, poke1.ataques, nome1)

                z(2)

                break

            else:
                nome2 = str(input('Digite o nome do treinador 2: ')).strip().capitalize()

                xx()

                escolhapokemon2 = menuu(f'{nome2}, escolha um dos 3 iniciais para usar na batalha: ', lista_pokemons())

                poke2 = Pokemon(escolhapokemon2, 35)

                treinador2 = Treinador(poke2.vida, poke2.ataques, nome2)

                z(2)

                break

        elif escolha == 5:
            xx()
            print('Até logo')
            sys.exit()

p1 = 0

while True: # Loop responsável pelo centro pokémon ou a pokémart.
    if p1 == 2:
        break
    
    if p1 == 0:
        xx()
        
        cabecalhonotebook(f'Treinador {nome1}, Seu pokémon possui {poke1.vida} de vida.')
        cabecalhonotebook(f'Você possui {treinador1.pokedollar} pokédollar.')
        z(1)
        print('\n')
        menudict2('Voçê possui esses itens:', treinador1.itens)
        z(1)
        print('\n')

        esc = menuu2('O que deseja fazer?', ['CENTRO POKÉMON', 'POKÉMART', 'SAIR'])

        if esc == 3:
            p1 += 1

        elif esc == 1:
            xx()
            cabecalhonotebook(f'{nome1}, a saúde do seu(ua) {poke1.nome} foi restaurada')
            poke1.vida = int(coisaspokemon1[6])
            z(2)

        elif esc == 2:
            while True:
                xx()
                preco = [50, 100, 200, 500]
                itens = ['potion', 'superpotion', 'hyperpotion', 'maxpotion']

                cabecalhonotebook(f'Voçê possui {treinador1.pokedollar} Pokédollar.')
                opp = menuu2('O que deseja comprar?', ['potion - 50 Pokédollar', 'superpotion - 100 Pokédollar', 'hyperpotion - 200 Pokédollar', 'maxpotion - 500 Pokédollar', 'SAIR'])

                if opp - 1 == 4:
                    break                    

                qtd = leiaint(f'\nQuantos(as){itens[opp - 1]} deseja comprar: ')

                total = preco[opp - 1] * qtd

                xx()

                if treinador1.pokedollar < preco[opp - 1]:
                    xx()
                    print('Dinheiro insuficiente...')
                    z(2)

                else:
                    xx()
                    cabecalhonotebook(f'Você comprou {itens[opp - 1]} por {total} Pokédollar.')
                    treinador1.itens[itens[opp - 1]][0] += qtd
                    z(2)


    elif p1 == 1:

        xx()
        
        cabecalhonotebook(f'Treinador {nome2}, Seu pokémon possui {poke2.vida} de vida.')
        cabecalhonotebook(f'Você possui {treinador1.pokedollar} pokédollar.')
        z(1)
        print('\n')
        menudict2('Voçê possui esses itens:', treinador2.itens)
        z(1)
        print('\n')
        esc = menuu2('O que deseja fazer?', ['CENTRO POKÉMON', 'POKÉMART', 'SAIR'])

        if esc == 3:
            p1 += 1

        elif esc == 1:
            xx()
            cabecalhonotebook(f'{nome2}, a saúde do seu(ua) {poke2.nome} foi restaurada')
            poke2.vida = int(coisaspokemon2[6])
            z(2)

        elif esc == 2:
            while True:
                xx()
                preco = [50, 100, 200, 500]
                itens = ['potion', 'superpotion', 'hyperpotion', 'maxpotion']

                cabecalhonotebook(f'Voçê possui {treinador2.pokedollar} Pokédollar.')
                opp = menuu2('O que deseja comprar?', ['potion - 50 Pokédollar', 'superpotion - 100 Pokédollar', 'hyperpotion - 200 Pokédollar', 'maxpotion - 500 Pokédollar', 'SAIR'])

                if opp - 1 == 4:
                    break                    

                qtd = leiaint(f'\nQuantos(as){itens[opp - 1]} deseja comprar: ')

                total = preco[opp - 1] * qtd

                xx()

                if treinador2.pokedollar < preco[opp - 1]:
                    xx()
                    print('Dinheiro insuficiente...')
                    z(2)

                else:
                    xx()
                    cabecalhonotebook(f'Você comprou {itens[opp - 1]} por {total} Pokédollar.')
                    treinador2.itens[itens[opp - 1]][0] += qtd
                    z(2)





turno = True   # True significa turno do poke1, False significa turno do poke2


while True: # Loop responsável pela batalha em si.
    if poke1.vida <= 0:
        xx()
        print(f'{poke1.nome} não pode continuar, vitória para o {poke2.nome}')
        salvar_informacoess(playerr1[1], poke1.nivel, 0, poke1.atk, poke1.defesa, poke1.velocidade, treinador1.itens, escolhapokemon1, treinador1.pokedollar, coisaspokemon1[6])
        salvar_informacoess(playerr2[1], poke2.nivel, poke2.vida, poke2.atk, poke2.defesa, poke2.velocidade, treinador2.itens, escolhapokemon2, treinador2.pokedollar, coisaspokemon2[6])
        break

    if poke2.vida <= 0:
        xx()
        print(f'{poke2.nome} não pode continuar, vitória para o {poke1.nome}')
        salvar_informacoess(playerr1[1], poke1.nivel, poke1.vida, poke1.atk, poke1.defesa, poke1.velocidade, treinador1.itens, escolhapokemon1, treinador1.pokedollar, coisaspokemon1[6])
        salvar_informacoess(playerr2[1], poke2.nivel, 0, poke2.atk, poke2.defesa, poke2.velocidade, treinador2.itens, escolhapokemon2, treinador2.pokedollar, coisaspokemon2[6])
        break


    if turno:
        xx()

        pokemonevida(escolhapokemon1, escolhapokemon2, poke1.vida, poke2.vida)

        z(1)

        turnopcao = menum(f'O que o {escolhapokemon1} do(a) {nome1} irá fazer?', ['LUTAR', 'MOCHILA', 'SAIR'])

        if turnopcao == 3:
            xx()
            print(f'{nome1} escolheu desistir, vitória para {nome2} e seu(ua) {escolhapokemon2}.')
            salvar_informacoess(playerr1[1], poke1.nivel, poke1.vida, poke1.atk, poke1.defesa, poke1.velocidade, treinador1.itens, escolhapokemon1, treinador1.pokedollar, coisaspokemon1[6])
            salvar_informacoess(playerr2[1], poke2.nivel, poke2.vida, poke2.atk, poke2.defesa, poke2.velocidade, treinador2.itens, escolhapokemon2, treinador2.pokedollar, coisaspokemon2[6])
            break

        elif turnopcao == 1:
            xx()
            pokemonevida(escolhapokemon1, escolhapokemon2, poke1.vida, poke2.vida)

            z(1)

            s = ataquedoturno(escolhapokemon1, poke1.ataques)

            poke2.vida = poke1.atacar(poke2.vida, poke2.defesa, poke1.ataques[s], poke2.tipo, poke1.nome)

            turno = False

            prosseguir()

        elif turnopcao == 2:
            xx()
            bag = menudict(f'MOCHILA DO {nome1}', treinador1.itens)

            if bag == 'sair':
                pass

            else:
                poke1.vida = treinador1.curavida(poke1.vida, treinador1.vidapokemon, bag)

                turno = False

        

    else:
        xx()

        pokemonevida(escolhapokemon1, escolhapokemon2, poke1.vida, poke2.vida)

        z(1)
        turnopcao = menum(f'O que {escolhapokemon2} do(a) {nome2} irá fazer?', ['LUTAR', 'MOCHILA', 'SAIR'])

        if turnopcao == 3:
            xx()
            print(f'{poke2.nome} decidiu desistir da batalha. A vitória vai para {treinador1.nome} e seu {poke1.nome}.')
            salvar_informacoess(playerr1[1], poke1.nivel, poke1.vida, poke1.atk, poke1.defesa, poke1.velocidade, treinador1.itens, escolhapokemon1, treinador1.pokedollar, coisaspokemon1[6])
            salvar_informacoess(playerr2[1], poke2.nivel, poke2.vida, poke2.atk, poke2.defesa, poke2.velocidade, treinador2.itens, escolhapokemon2, treinador2.pokedollar, coisaspokemon2[6])
            break

        elif turnopcao == 1:
            xx()
            pokemonevida(escolhapokemon1, escolhapokemon2, poke1.vida, poke2.vida)

            z(1)

            s = ataquedoturno(escolhapokemon2, poke2.ataques)

            poke1.vida = poke2.atacar(poke1.vida, poke1.defesa, poke2.ataques[s], poke1.tipo, poke2.nome)

            turno = True

            prosseguir()

        elif turnopcao == 2:
            xx()
            bag = menudict(f'MOCHILA DO {nome2}', treinador2.itens)

            if bag == 'sair':
                pass

            elif turnopcao == 2:
                poke2.vida = treinador2.curavida(poke2.vida, treinador2.vidapokemon, bag)

                turno = True

            
