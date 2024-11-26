"""
2. Easy: Create a class 'Animal' with a method 'speak()'. 
Create two derived classes 'Dog' and 'Cat' that override the speak method.
Dog should return "Woof!" and Cat should return "Meow!"
"""
import unittest
import math

class Animal:
    def speak(self):
        return ""
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
class TestAnimals(unittest.TestCase):
    def test_animal_speak(self):
        animal = Animal()
        self.assertEqual(animal.speak(), "")
    
    def test_dog_speak(self):
        dog = Dog()
        self.assertEqual(dog.speak(), "Woof!")
    
    def test_cat_speak(self):
        cat = Cat()
        self.assertEqual(cat.speak(), "Meow!")

if __name__ == '__main__':
    unittest.main()