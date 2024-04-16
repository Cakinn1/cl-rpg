from Player import Player
from Enemy import Enemy
class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        
    def run_battle(self):
        print(f"A battle beings with {self.enemy.name}")
        while self.player.health > 0 and self.enemy.health > 0:
            # players turn
            print("It's your turn!")
            self.player.use_ability(self.enemy)
            print("")
            
            if self.enemy.health > 0:
                print(f"The {self.enemy.name} strikes back!")
                
                self.enemy.random_attack(self.player)
            
            print(f"players health: {self.player.health}, enemys health: {self.enemy.health}")
            print("")
            
         # fix this after just temp so console doesnt call "None"
        return False
            
            
    
    
    
player = Player(character_class="mage")
goblin = Enemy(name="goblin", health=100, mana=20, attack=4, defense=4)
battle = Battle(player, goblin)


print(battle.run_battle())  
    
    