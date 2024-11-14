
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
    pass

class Warrior(Character):
    pass

class Mage(Character):
    pass

class Archer(Character):
    pass

class TestGameCharacters(unittest.TestCase):
    def test_characters(self):
        warrior = Warrior()
        self.assertEqual(warrior.attack(), 15)
        self.assertEqual(warrior.use_special_ability(), "Warrior uses Berserk!")
        
        mage = Mage()
        self.assertEqual(mage.use_special_ability(), "Mage casts Fireball!")
        
        archer = Archer()
        self.assertEqual(archer.use_special_ability(), "Archer uses Rapid Shot!")

if __name__ == '__main__':
    unittest.main()