from random import randint, uniform
from funcoes import *

# Patch note no articuno que ta roubado.

class Pokemon:
    def __init__(self, nome, nivel):
        self.nivel = nivel
        self.nome = nome  

        # {Nome do ataque : [tipo do ataque, dano do ataque, PP do ataque, acuracy do ataque]}


        match(nome):
            case 'charmander':
                self.vida = 188
                self.vidaoriginal = 188
                self.atk = 98
                self.defesa = 81
                self.velocidade = 121 
                self.tipo = ['fire']
                self.ataques = {'scratch': ['normal', 40, 35, 100], 'ember':['fire', 40, 25, 100], 'rage':['normal', 20, 20, 100], 'slash':['normal', 70, 20, 100]}
                # self.pp = {'scratch': ['normal', 40, 35], 'ember':['fire', 40, 25], 'rage':['normal', 20, 20], 'slash':['normal', 70, 20]}
            
            case 'squirtle': 
                self.vida = 198
                self.vidaoriginal = 198
                self.atk = 90
                self.defesa = 121
                self.velocidade = 81 
                self.tipo = ['water']
                self.ataques = {'tackle':['normal', 35, 35, 100], 'bubble':['water', 20, 30, 100], 'water gun':['water', 40, 25, 100], 'bite':['normal', 60, 25, 100]}
                # self.pp = {'tackle':['normal', 35, 35], 'bubble':['water', 20, 30], 'water gun':['water', 40, 25], 'bite':['normal', 60, 25]}
           
            case 'bulbasaur': 
                self.vida = 200
                self.vidaorigial = 200
                self.atk = 92
                self.defesa = 92
                self.velocidade = 85 
                self.tipo = ['grass']
                self.ataques = {'tackle':['normal', 35, 35, 100], 'solarbeam':['grass', 120, 10, 100], 'vine whip':['grass', 35, 10, 100], 'razor leaf':['grass', 55, 25, 100]}
                # self.pp = {'tackle':['normal', 35, 35], 'solarbeam':['grass', 120, 10], 'vine whip':['grass', 35, 10], 'razor leaf':['grass', 55, 25]}
            
            case 'pikachu':
                self.vida = 180
                self.vidaorigial = 180
                self.atk = 103
                self.defesa = 76
                self.velocidade = 85 
                self.tipo = ['electric']
                self.ataques = {'quick attack':['normal', 40, 30, 100], 'iron tail':['steel', 100, 15, 75], 'thunder shock':['electric', 40, 30, 100], 'thunder':['electric', 110, 10, 70]}

            case 'butterfree':
                self.vida = 230
                self.vidaorigial = 230
                self.atk = 85
                self.defesa = 94
                self.velocidade = 130 
                self.tipo = ['bug','flying']
                self.ataques = {'gust':['flying', 40, 35, 100], 'confusion':['psychic', 50, 25, 100], 'air slash':['flying', 75, 20, 95], 'bug buzz':['electric', 90, 10, 100]}

            case 'articuno':
                self.vida = 290
                self.vidaorigial = 290
                self.atk = 157
                self.defesa = 184
                self.velocidade = 157 
                self.tipo = ['ice','flying']
                self.ataques = {'powder snow':['ice', 40, 25, 100], 'confusion':['psychic', 50, 25, 100], 'air slash':['flying', 75, 20, 95], 'blizzard':['electric', 100, 5, 70]}



    def atacar(self, vida, defesa, ataque, tipooponente, donodoturno):

        # (Self, Vida do oponente, defesa do oponente, ataque utilizado, tippo do oponente)

        # Quanto de dano o pokémon vai dar.


        if ataque[3] < randint(0, 100):
            xx()
            print('\033[31mATAQUE FALHOU!!!\033[m')
            return vida

        critico = randint(0, 255) < self.velocidade / 2
        ataque[2] -= 1
        ale = round(uniform(0.85, 1), 2)
        dano = (((2 * self.nivel + 10)/250) * (self.atk/defesa)* ataque[1] + 2) * ale

        double = False
        half = False
        null = False

        tipos = {
            'fire' : [['bug', 'steel', 'grass', 'ice', 'fairy'], ['ground', 'rock', 'water'],[]], 
            'water' : [['steel' , 'fire', 'water', 'ice'], ['grass', 'electric'], []],
            'grass' : [['ground', 'water', 'grass', 'electric'], ['flying', 'poison', 'bug', 'fire', 'ice'], []],
            'electric' : [['flying', 'steel', 'electric'], [], []],
            'normal' : [[], ['fighting'], ['ghost']],
            'fighting' : [['rock', 'bug', 'dark'], ['fairy'], []],
            'flying' : [['fighting', 'bug', 'grass'], ['rock', 'electric', 'ice'], ['ground']],
            'poison' : [['fighting', 'poison', 'bug', 'grass', 'fairy'], ['ground', 'psychic'], []],
            'ground' : [['poison', 'rock'], ['water', 'grass', 'ice'], ['electric']],
            'rock' : [['normal', 'flying', 'poison', 'fire'], ['fighting', 'ground', 'steel', 'water', 'grass'], []],
            'bug' : [['fighting', 'ground', 'grass'], ['flying', 'rock', 'fire'], []],
            'ghost' : [['poison', 'bug'], ['ghost', 'dark'], ['normal', 'fighting']],
            'steel' : [['normal', 'flying', 'rock', 'bug', 'steel', 'grass', 'psychic', 'ice', 'dragon', 'fairy'], ['fighting', 'ground', 'fire'], ['poison']],
            'psychic' : [['fighting', 'psychic'], ['bug', 'ghost', 'dark'], []],
            'ice' : [['ice'], ['fighting', 'rock', 'steel', 'fire'], []],
            'dragon' : [['fire', 'water', 'grass', 'electric'], ['ice', 'dragon', 'fairy'], []],
            'dark' : [['ghost', 'dark'], ['fighting', 'bug', 'fairy'], ['psychic']],
            'fairy' : [['fighting', 'bug', 'dark'], ['poison', 'steel'], ['dragon']]
        }

        if critico:
            dano *= 2
            
        for tp in tipooponente:

            if ataque[0] in tipos[tp][0]:
                dano *= 0.5
            elif ataque[0] in tipos[tp][1]:
                dano *= 2
            elif ataque[0] in tipos[tp][2]:
                dano *= 0
            
            if self.tipo == ataque[0]:
                dano *= 1.5
        

        xx()

        print(f'\n{donodoturno} causou {int(dano)} de dano')
        return vida - int(dano)


    def atualizar_status(self, lst):
        self.vida = int(lst[2])
        self.atk = int(lst[3])
        self.defesa = int(lst[4])
        self.velocidade = int(lst[5])


def lista_pokemons():
    lst = ['charmander', 'squirtle', 'bulbasaur', 'pikachu', 'butterfree']

    return lst