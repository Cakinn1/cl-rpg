class Entity:
    def __init__(self, health=100, mana=5, level=0,  attack=8, defense=5, ):
        self.health = health
        self.level = level
        self.attack = attack
        self.mana = mana
        self.defense = defense
        ...