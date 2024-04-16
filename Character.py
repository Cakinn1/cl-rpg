class Character:
    def __init__(self, health=100, mana=5, level=0,  attack=8, defense=5, ):
        self.health = health
        self.level = level
        self.attack = attack
        self.mana = mana
        self.defense = defense
        ...
        
        
    def attack_user(self, target):
        damage = self.attack - target.defense
        target.health -= damage
        ...
        
    def gain_xp(self, amount):
        # amount of xp gained 
        self.xp += amount
        self.check_level_up() # check if character can level up
               

        

    @property
    def view_stats(self):
        return {
            "Strength": self.strength, 
            "Dexterity": self.dexterity, 
            "Intelligence": self.intelligence,
            "Health": self.health,
            "Level": self.level,
            "XP": self.xp,
            "Class": self.character_class,
            "Attack": self.attack
            }



# class Character:
#     def __init__(self, strength=1,  dexterity=1, intelligence=1, health=100, mana=5, level=0, xp=0, attack=8, defense=5, character_class=None):
#         self.strength = strength
#         self.dexterity = dexterity
#         self.intelligence = intelligence
#         self.health = health
#         self.level = level
#         self.xp = xp
#         self.attack = attack
#         self.mana = mana
#         self.defense = defense
#         self.character_class = character_class
#         self.xp_to_next_level = 10
#         ...
        
        
#     def attack_user(self, target):
#         damage = self.attack - target.defense
#         target.health -= damage
#         ...
        
#     def gain_xp(self, amount):
#         # amount of xp gained 
#         self.xp += amount
#         self.check_level_up() # check if character can level up
               
#     def level_up(self):
#         if self.character_class == "Warrior":
#             # increase states related to warrior by 50% else only 20%
#             self.strength *= 1.5
#             self.attack *= 1.5
#             self.health *= 1.5
#             self.defense *= 1.5
#             self.intelligence *= 1.2
#             self.dexterity *= 1.2
#         elif self.character_class == "Mage":
#             self.attack *= 1.8
#             self.strength *= 1.2
#             self.health *= 1.2
#             self.defense *= 1.1
#             self.intelligence *= 2
#             self.dexterity *= 1.2
        
        
        
#     def check_level_up (self):
#         if self.xp > self.xp_to_next_level:
#             self.level += 1
#             self.level_up()
#             # increse xp needed by 20% to get to next level
#             self.xp_to_next_level *= 1.2
 
        

#     @property
#     def view_stats(self):
#         return {
#             "Strength": self.strength, 
#             "Dexterity": self.dexterity, 
#             "Intelligence": self.intelligence,
#             "Health": self.health,
#             "Level": self.level,
#             "XP": self.xp,
#             "Class": self.character_class,
#             "Attack": self.attack
#             }
        

