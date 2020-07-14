
#DEFINE POKEMON CLASS
class Pokemon:
    def __init__(self, name, ptype, level):
        self.name = name
        self.level = level
        self.ptype = ptype
        self.max_heath = 10 * level
        self.health = 10 * level
        self.battle_experience = 0
        self.is_knocked_out = False

    #Pokemon lose health
    def lose_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.knock_out()
        print('{name} current health is: {health}'.format(name = self.name, health = self.health))  

    #Pokemon gain health but should not exceed max_health
    def gain_health(self, amount):
        if self.gain_health <= self.level:
            self.revive()
        self.health += amount
        if self.health >= self.max_heath:
            self.health = self.max_heath
        print('{name} have {health} of health now'.format(name = self.name, health = self.health))
    
    #Pokemon knock out & health assign to 0
    def knock_out(self):
        self.is_knocked_out = True
        self.health = 0
        print('{name} has been knocked out'.format(name = self.name))

    #Pokemon revive health
    def revive(self):
        self.is_knocked_out = False
        self.health = 10
        print('{name} has revive with {health} health'.format(name = self.name, health = self.health))

    #Pokemon attack
    def attack(self, opponent):
        #oppenent has advantage
        def opponent_adv(self, opponent):
            damage_equal = round(self.level * 2)
            opponent.lose_health(damage_equal)
            print('{name} attacked {opponent} with advantage and damage {damage} points'.format(name = self.name, opponent = opponent.name, damage = damage_equal))
            
            self.battle_experience += 5
            if self.battle_experience >= 20:
                self.level += 1
                self.battle_experience = 0
                print('{name} leveled up!'.format(name = self.name))

        #oppenent has disadvantage
        def opponent_disAdv(self, opponent):
            damage_equal = round(self.level * 0.5)
            opponent.lose_health(damage_equal)
            print('{name} attacked {opponent} with disadvantage and damage {damage} points'.format(name = self.name, opponent = opponent.name, damage = damage_equal))
            self.battle_experience += 4
            if self.battle_experience >= 20:
                self.level += 1
                self.battle_experience = 0
                print('{name} leveled up!'.format(name = self.name))

        if self.is_knocked_out:
            print('{name} is knocked out, can not attack {opp}!'.format(name = self.name, opp = opponent.name))
        elif opponent.is_knocked_out:
            print('{opp} is knocked out!, can not attack {name}'.format(name = self.name, opp = opponent.name))
        #Pokemon offense advantage types
        elif self.ptype == opponent.ptype or self.ptype == 'Fire' and opponent.ptype == 'Grass' or self.ptype == 'Water' and opponent.ptype == 'Fire' or self.ptype == 'Grass' and opponent.ptype == 'Water':
            opponent_adv(self, opponent)
        #Pokemon offense disadvantage types
        elif self.ptype == 'Fire' and opponent.ptype == 'Water' or self.ptype == 'Water' and opponent.ptype == 'Grass' or self.ptype == 'Grass' and opponent.ptype == 'Fire':
            opponent_disAdv(self, opponent)

#DEFINE TRAINER CLASS
class Trainer:
    def __init__(self, name, pokemon_list, potions = 3):
        self.pokemons = pokemon_list
        self.name = name
        self.potions = potions
        self.current_pokemon = 0

    #Use potion and revive a knocked out Pokemon
    def potion(self, potion):
        if self.potions > 0:
            self.potions -= potion
            print('{name} used a potion'.format(name = self.pokemons[self.current_pokemon].name))
            
            #Revive Pokemon if it's health = 0
            if not self.pokemons[self.current_pokemon].is_knocked_out:
                self.pokemons[self.current_pokemon].gain_health(10)
                print('{name} has gain health'.format(name = self.pokemons[self.current_pokemon].name))
            else:
                self.pokemons[self.current_pokemon].revive()
                #print('{name} has been revived'.format(name - self.pokemons[self.current_pokemon].name))
            if self.pokemons[self.current_pokemon].health > self.pokemons[self.current_pokemon].max_heath:
                self.pokemons[self.current_pokemon].health = self.pokemons[self.current_pokemon].max_heath
        else:
            print('No more potions left!')    
    
    #Attack another trainer's Pokemon
    def attack_opp(self, opponent_trainer):
        self.pokemons[self.current_pokemon].attack(opponent_trainer.pokemons[opponent_trainer.current_pokemon])
        print('{name} trainer has been attacked'.format(name = opponent_trainer.name))

    #Switch current pokemon to another in your list
    def switch_pokemon(self, new_pokemon):
        if new_pokemon <= len(self.pokemons) and new_pokemon >= 0:
            if self.pokemons[new_pokemon].is_knocked_out:
                print('choose another pokemon, {name} has been knocked'.format(name = self.pokemons[new_pokemon].name))
            elif self.pokemons[new_pokemon] == self.pokemons[self.current_pokemon]:
                print('switching to the same pokemon {name}'.format(name = self.pokemons[new_pokemon].name))
            elif self.pokemons[new_pokemon] != self.pokemons[self.current_pokemon]:
                self.current_pokemon = new_pokemon
                print('Has been switch to {name} pokemon'.format(name = self.pokemons[new_pokemon].name))
        else:
            print('No pokemon available to switch!')


#POKEMON TO PLAY
#  Lotad = Pokemon('Lotad', 'Grass', level = 7)
Pikachu = Pokemon('Pikachu', 'Fire', level = 5)
Charzard = Pokemon('Charzard', 'Water', level = 2)
Squirtle = Pokemon('Squirtle', 'Grass', level = 7)
Snorlax = Pokemon('Snorlax', 'Fire', level = 1)


Jo = Trainer('Jo', [Pikachu, Snorlax], potions = 5)
Dom = Trainer('Do', [Squirtle, Charzard], potions = 9)
Braia = Trainer('Braia', [Snorlax, Charzard], potions = 1)
Seya = Trainer('Seya', [Squirtle, Pikachu], potions = 3)

#Testing attacking
Jo.attack_opp(Seya)
Braia.attack_opp(Dom)

#Testing using potions
Pikachu.knock_out()
Jo.potion(1)

#Testing switching Pokemon
Snorlax.knock_out()
Braia.switch_pokemon(0)
Braia.switch_pokemon(1)