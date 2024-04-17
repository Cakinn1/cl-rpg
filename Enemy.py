from Ability import Ability
import random 

class Enemy:
    ENEMY_GOBLIN = "goblin"
    ENEMY_TROLL = "troll"
    ENEMY_BOSS = "warlord_boss"
    def __init__(self, name, health, mana, attack, defense, level):
        self.name = name  
        self.health = health
        self.mana = mana
        self.attack = attack
        self.defense = defense
        self.level = level
        self.abilities = []
        if name == self.ENEMY_GOBLIN:
            self.abilities.append(Ability("basic_attack", damage=8 + self.attack, mana_cost=0))
            self.abilities.append(Ability("goblin_attack", damage=12 + self.attack, mana_cost=2))
    
    
    def random_attack(self, target):
        choosen_ability = random.choice(self.abilities)
        choosen_ability.use(self, target)
        return choosen_ability
        

