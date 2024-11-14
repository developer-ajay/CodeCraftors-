import unittest

class Animal:
    def speak(self):
        return ""

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


dog = Dog()
cat = Cat()

print(f"Dog says: {dog.speak()}")  
print(f"Cat says: {cat.speak()}")  

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

