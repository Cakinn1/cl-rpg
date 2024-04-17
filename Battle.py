from Player import Player
from Enemy import Enemy
import sys
import random

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        
                
    def check_battle_over(self):
        if self.player.health <= 0:
            print(f"{self.enemy.name} has defated you, Game over...")
            sys.exit()
        elif self.enemy.health <= 0:
            print("You have won the battle!")   
            self.player.xp += self.enemy.level
            self.player.check_level_up()
            if random.randint(1, 100) <= 50:
                loot_options = ["health potion", "mana potion", "health potion", "mana potion"]
                loot = random.choice(loot_options)
                self.player.inventory.append(loot)
                print(f"{self.enemy.name} has dropped {loot}")
            print("")
            return True
        else:
            return False
    
    
    def player_turn(self):
        print("It's your turn!")
        self.player.use_ability(self.enemy)
        print("")
        
        
    def enemy_turn(self):
        print(f"The {self.enemy.name} strikes back!")
        self.enemy.random_attack(self.player)
        
    def run_battle(self):
        print("")
        print(f"A battle beings with {self.enemy.name}")
        
        while True:
            self.player_turn()
            if self.check_battle_over():
                break
            
            self.enemy_turn()
            if self.check_battle_over():
                break
                
            print(f"players health: {self.player.health}")
            print(f"{self.enemy.name} health: {self.enemy.health}")
            print('')
                
    








        
    
        
