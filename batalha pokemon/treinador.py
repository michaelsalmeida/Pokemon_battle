from funcoes import *


class Treinador:
    def __init__(self, vidapokemon, vidapokemonoriginal, atkspokemon, nome):
        self.nome = nome 
        self.pokedollar = 0
        self.vidapokemon = vidapokemon
        self.vidapokemonoriginal = vidapokemonoriginal
        self.atkspokemon = atkspokemon
        self.itens = {'potion' : [5, 20], 'superpotion' : [5, 50], 'hyperpotion' : [1, 200], 'maxpotion' : [1, self.vidapokemonoriginal]}
        self.potion = [5, 20]                    #[quantidade, quanto cura]   /   HP + 20
        self.superpotion = [5, 50]               #[quantidade, quanto cura]  /    HP + 50
        self.hyperpotion = [1, 200]              #[quantidade, quanto cura]  /    HP + 200
        self.maxpotion = [1, self.vidapokemon]   #[quantidade, quanto cura]   /   HP + FULL

        self.ether = [5, 10]                     # PP + 10
       
        #self.maxether = 2     # PP + FULL
        #self.elixir = 1       # PP de todos os ataques full

        


    def curavida(self, vidaatual, vidatotal, itemescolhido):
        itens = self.itens
        if vidaatual == vidatotal:
            print('Vida já está cheia.')
            z(2)
            return vidaatual

        elif itens[itemescolhido][0] == 0:
            xx()
            print(f'Você não possui mais {itemescolhido} disponível')
            z(2)
            return vidaatual

        elif vidaatual + itens[itemescolhido][1] > vidatotal:
            itens[itemescolhido][0] -= 1
            return vidatotal

        else:
            vidaa = vidaatual + itens[itemescolhido][1]
            itens[itemescolhido][0] -= 1
            return vidaa

    def atualizar_itens(self, lst):
        self.itens['potion'][0] = int(lst[0])
        self.itens['superpotion'][0] = int(lst[1])
        self.itens['hyperpotion'][0] = int(lst[2])
        self.itens['maxpotion'][0] = int(lst[3])
        self.pokedollar = int(lst[4])