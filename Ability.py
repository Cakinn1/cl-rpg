class Ability:
    def __init__(self, name, damage=0, mana_cost=0, success_rate=100):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.success_rate = success_rate
        ...
        def __str__(self):
            return f"{self.name} (Mana: {self.mana_cost}, Damage: {self.damage})"
        
        
    def use(self, user, target):
        if user.mana <= self.mana_cost:
            print("Not enough mana")
            return True
        else:
            target.health -= self.damage
            user.mana -= self.mana_cost
        
        # add failing success rate here
        # and add a way for the cmoputer to use this class too
        

        
    def attack_name(self):
        return f"{self.name}"
        
    ...