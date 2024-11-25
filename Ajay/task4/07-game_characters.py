class Character:
    def __init__(self, health , damage , special_ability ):
        self.health = health
        self.damage = damage
        self.special_ability = special_ability
        
    def attack(self):
        return f"{self,__class__.__name__} attacks & {self.damage} damage!! "
    
    def use_special_ability(self):
        return f"{self.__class__.__name__} uses special ability: {self.special_ability}"


class Warrior(Character):
    def __init__(self, health, damage, special_ability):
        super().__init__(health, damage, special_ability)

    def attack(self):
        print(f"Warrior swings sword and deals {self.damage} damage!")

    def use_special_ability(self):
        print(f"Warrior uses 'Rage' to double damage for one turn!")


class Mage(Character):
    def __init__(self, health, damage, special_ability):
        super().__init__(health, damage, special_ability)

    def attack(self):
        print(f"Mage casts a spell dealing {self.damage} damage!")

    def use_special_ability(self):
        print(f"Mage uses 'Fireball' to deal massive area damage!")


class Archer(Character):
    def __init__(self, health, damage, special_ability):
        super().__init__(health, damage, special_ability)

    def attack(self):
        print(f"Archer shoots an arrow dealing {self.damage} damage!")

    def use_special_ability(self):
        print(f"Archer uses 'Multi-Shot' to hit multiple enemies at once!")


warrior = Warrior(100, 25, "Rage")
mage = Mage(80, 20, "Fireball")
archer = Archer(70, 15, "Multi-Shot")


warrior.attack()
warrior.use_special_ability()

mage.attack()
mage.use_special_ability()

archer.attack()
archer.use_special_ability()