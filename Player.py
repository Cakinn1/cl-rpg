from Entity import Entity
from Ability import Ability
import sys
class Player(Entity):
    HEALTH_POTION_AMOUNT = 40
    MANA_POTION_AMOUNT = 10
    WARRIOR_CLASS = 'warrior'
    MAGE_CLASS = 'mage'
    
    def __init__(self, strength=1,  dexterity=1, intelligence=1, xp=0, character_class=None, name=None):
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.xp = xp
        self.character_class = character_class
        self.name = name
        self.inventory = ["health potion"]
        self.abiilities = []
        self._initialize_player_stats()
        

    def add_starter_abilities(self):
        stats_damage = self.intelligence + self.attack
        if self.character_class == self.MAGE_CLASS:
            self.abiilities.append(Ability('fireball', damage=20 + stats_damage, mana_cost=2))
            self.abiilities.append(Ability("fire_wall", damage=30 + stats_damage, mana_cost=3))
            self.abiilities.append(Ability("basic_attack", damage=5 + stats_damage, mana_cost=0))
        elif self.character_class == self.WARRIOR_CLASS:
            self.abiilities.append(Ability("sword_strike", damage=20 + stats_damage, mana_cost=2))
            self.abiilities.append(Ability("heavenly_sword", damage=40 + stats_damage, mana_cost=8))
            self.abiilities.append(Ability("basic_attack", damage=8 + stats_damage, mana_cost=0))
    
    def use_ability(self, enemy):
        for i in range(len(self.abiilities)):
            print(f"{i + 1}. {self.abiilities[i].name} (Mana: {self.abiilities[i].mana_cost}, Damage: {self.abiilities[i].damage})")
            
        while True:
            choice = input("Choose an ability (or 'b' to exit): ") 
            # add nbetter error handling here
            
            if choice == "b":
                # for some reason break and return is not working
                # temp fix for now need to figure out what is going on wrong
                sys.exit()
            elif choice.isdigit() and int(choice) > 0 and int(choice) <= len(self.abiilities):
                choosen_ability_index = int(choice) - 1
                self.abiilities[choosen_ability_index].use(self, enemy)
                break
            else:
                print("Invalid choice. Please enter a number between 1 and", len(self.abiilities))
                
               
    
    def _initialize_player_stats(self):
        self.xp_to_next_level = 10
        self.health = 100
        self.mana = 60
        self.level = 1
        self.attack = 8
        self.defense = 5
        super().__init__(self.health, self.mana, self.level, self.attack, self.defense)

    def check_level_up (self):
        if self.xp >= self.xp_to_next_level:
            self.level += 1
            self.level_up()
            self.xp_to_next_level *= 1.2
            self.xp = 0
            self.level_up_anaimation()
            ...
        else:
            xp_left_till_level_up = self.xp / self.xp_to_next_level * 100
            print(f"Your're {xp_left_till_level_up:.0f}% of the way to level {self.level + 1}!")
        
            
    def level_up_anaimation(self):
        print("")
        print("##############################################")
        print("You have leveled up!")
        print(f"You are currently level: {self.level}")
        print(f"Here are your new stats: {self.view_stat}")
        print("##############################################")
        print("")

    def level_up(self):
        if self.character_class == self.WARRIOR_CLASS:
            self.increase_stats(
                {"attack": 2, "health": 1.6, "mana": 0.2, 
                "defense": 1.4, "strength": 1.4,
                "intelligence": 0.3, "dexterity": 0.4
                },
                )
        elif self.character_class == self.MAGE_CLASS:
            self.increase_stats(
               {"attack": 1.1, "health": 1.1, "mana": 2, 
                "defense": 1.1, "strength": 1.1, 
                "intelligence": 2.2, "dexterity": 1.1
                }
               ,)
    @property        
    def view_stat(self):
        abilities_info = [f"{ability.name} (Mana: {ability.mana_cost}, Damage: {ability.damage})" for ability in self.abiilities]
            
        return {
            "Strength": self.strength, 
            "Dexterity": self.dexterity, 
            "Intelligence": self.intelligence,
            "Health": self.health,
            "Level": self.level,
            "XP": self.xp,
            "Class": self.character_class,
            "Attack": self.attack,
            "Abilities": abilities_info,
            "mana": self.mana
            }
            
    def increase_stats (self, stat_increase):
        for stat, multipiler in stat_increase.items():
            current_value = getattr(self, stat) # get the current value of the stat
            setattr(self, stat, current_value * multipiler) # update the stat
            
    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item}, added to inventory {self.inventory}")
    
    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{item} removed")
            return True
        else:
            print(f"{item} Not in Inventory")
            return False
            
    def use_potion(self, potion_type):
        try:
            self.inventory.remove(potion_type)
            self.apply_potion_effects(potion_type)
            return True
        except ValueError:  # ValueError occurs if the item is not in the list
            print(f"Failed to use {potion_type}!")
        except Exception as e: 
            print(f"An error occurred while using a potion: {e}")
            
  
            
    def apply_potion_effects (self, potion_type):
        if potion_type == "health potion":
            self.health += self.HEALTH_POTION_AMOUNT
            print(f"Current Health: {self.health}")
        elif potion_type == "mana potion":
            self.mana += self.MANA_POTION_AMOUNT
            print(f"Current Mana: {self.mana}")
