"""
7. Medium: Implement a class hierarchy for a simple game with characters:
Base class 'Character' and derived classes 'Warrior', 'Mage', and 'Archer'.
Each class should have:
- health, damage, and special_ability
- attack() method
- use_special_ability() method
"""
import unittest
import math
class Character:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage
    
    def attack(self):
        return self.damage
    
    def use_special_ability(self):
        pass

class Warrior(Character):
    def __init__(self):
        super().__init__(health=100, damage=15)
    
    def use_special_ability(self):
        return "Warrior uses Berserk!"

class Mage(Character):
    def __init__(self):
        super().__init__(health=70, damage=20)
    
    def use_special_ability(self):
        return "Mage casts Fireball!"

class Archer(Character):
    def __init__(self):
        super().__init__(health=80, damage=18)
    
    def use_special_ability(self):
        return "Archer uses Rapid Shot!"

class TestGameCharacters(unittest.TestCase):
    def test_characters(self):
        warrior = Warrior()
        self.assertEqual(warrior.attack(), 15)
        self.assertEqual(warrior.use_special_ability(), "Warrior uses Berserk!")
        
        mage = Mage()
        self.assertEqual(mage.use_special_ability(), "Mage casts Fireball!")
        
        archer = Archer()
        self.assertEqual(archer.use_special_ability(), "Archer uses Rapid Shot!")