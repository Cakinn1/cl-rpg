from Character import Character
class Player(Character):
    def __init__(self, strength=1,  dexterity=1, intelligence=1, xp=0, character_class=None):
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.xp = xp
        self.character_class = character_class
        self.xp_to_next_level = 10
        
        
        super().__init__(strength, dexterity, intelligence, health, mana, level, xp, attack, defense, character_class)
    ...
    
