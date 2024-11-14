# Easy Questions Solutions (1-3)

"""
1. Solution: Shape Inheritance
"""
import unittest
import math

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class TestShapes(unittest.TestCase):
    def test_shape_area(self):
        shape = Shape()
        self.assertEqual(shape.area(), 0)
    
    def test_square_area(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)
    
    def test_circle_area(self):
        circle = Circle(2)
        self.assertEqual(circle.area(), 12.56)

"""
2. Solution: Animal Polymorphism
"""
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

"""
3. Solution: Calculator with Static Methods
"""
class Calculator:
    @staticmethod
    def add(*args):
        return sum(args) if args else 0
    
    @staticmethod
    def multiply(*args):
        if not args:
            return 1
        result = 1
        for num in args:
            result *= num
        return result

class TestCalculator(unittest.TestCase):
    def test_no_args(self):
        self.assertEqual(Calculator.add(), 0)
        self.assertEqual(Calculator.multiply(), 1)
    
    def test_single_arg(self):
        self.assertEqual(Calculator.add(5), 5)
        self.assertEqual(Calculator.multiply(5), 5)
    
    def test_multiple_args(self):
        self.assertEqual(Calculator.add(1, 2, 3), 6)
        self.assertEqual(Calculator.multiply(2, 3, 4), 24)

# Medium Questions Solutions (4-5)

"""
4. Solution: Banking System
"""
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    def calculate_interest(self):
        return self.balance * self.interest_rate
    
    def withdraw(self, amount):
        if self.balance - amount < 0:
            raise ValueError("Insufficient funds")
        return super().withdraw(amount)

class CheckingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            raise ValueError("Exceeded overdraft limit")
        self.balance -= amount
        return True

class TestBankAccounts(unittest.TestCase):
    def test_savings_account(self):
        savings = SavingsAccount(1001, 1000, 0.05)
        self.assertEqual(savings.calculate_interest(), 50)
        savings.withdraw(500)
        self.assertEqual(savings.balance, 500)
        with self.assertRaises(ValueError):
            savings.withdraw(1000)
    
    def test_checking_account(self):
        checking = CheckingAccount(2001, 1000, 200)
        checking.withdraw(1100)
        self.assertEqual(checking.balance, -100)
        with self.assertRaises(ValueError):
            checking.withdraw(300)

"""
5. Solution: Vector3D with Operator Overloading
"""
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Vector3D(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )
    
    def __mul__(self, other):
        # Dot product
        return (self.x * other.x +
                self.y * other.y +
                self.z * other.z)
    
    def __eq__(self, other):
        return (self.x == other.x and
                self.y == other.y and
                self.z == other.z)
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

class TestVector3D(unittest.TestCase):
    def test_operations(self):
        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(4, 5, 6)
        self.assertEqual(str(v1), "(1, 2, 3)")
        self.assertEqual(str(v1 + v2), "(5, 7, 9)")
        self.assertEqual(v1 * v2, 32)
        self.assertTrue(v1 == Vector3D(1, 2, 3))
        self.assertFalse(v1 == v2)

# Medium Questions Solutions (6-7)

"""
6. Solution: Vehicle Abstract Base Class
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self):
        self.fuel_level = 0
        self.is_running = False
    
    @abstractmethod
    def get_fuel_capacity(self):
        pass
    
    def start_engine(self):
        if self.fuel_level > 0:
            self.is_running = True
            return True
        return False
    
    def stop_engine(self):
        self.is_running = False
        return True
    
    def fuel_up(self, amount):
        capacity = self.get_fuel_capacity()
        available_space = capacity - self.fuel_level
        if amount <= available_space:
            self.fuel_level += amount
            return f"Fueled up {amount}L"
        else:
            self.fuel_level = capacity
            return f"Fueled up {available_space}L. Tank full."

class Car(Vehicle):
    def get_fuel_capacity(self):
        return 45

class Motorcycle(Vehicle):
    def get_fuel_capacity(self):
        return 15

class Truck(Vehicle):
    def get_fuel_capacity(self):
        return 200

class TestVehicles(unittest.TestCase):
    def test_vehicles(self):
        car = Car()
        self.assertTrue(car.start_engine() == False)  # No fuel
        self.assertEqual(car.fuel_up(50), "Fueled up 45L. Tank full.")
        self.assertTrue(car.start_engine())
        self.assertTrue(car.stop_engine())
        
        motorcycle = Motorcycle()
        self.assertEqual(motorcycle.fuel_up(20), "Fueled up 15L. Tank full.")
        
        truck = Truck()
        self.assertEqual(truck.fuel_up(200), "Fueled up 200L")

"""
7. Solution: Game Character Hierarchy
"""
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

# Hard Questions Solutions (8-10)

"""
8. Solution: Database Error Hierarchy
"""
class DatabaseError(Exception):
    def __init__(self, message, **kwargs):
        super().__init__(message)
        self.details = kwargs

class ConnectionError(DatabaseError):
    def __str__(self):
        return f"{super().__str__()} to {self.details['host']}:{self.details['port']}"

class QueryError(DatabaseError):
    def __init__(self, message, query):
        super().__init__(message, query=query)
    
    def get_position(self):
        # Find position of first error in query
        return self.details['query'].find("FORM")  # Simple example

class DataError(DatabaseError):
    pass

class TestDatabaseErrors(unittest.TestCase):
    def test_exceptions(self):
        with self.assertRaises(ConnectionError) as context:
            raise ConnectionError("Failed to connect", host="localhost", port=5432)
        self.assertEqual(str(context.exception), "Failed to connect to localhost:5432")
        
        with self.assertRaises(QueryError) as context:
            raise QueryError("Invalid SQL", query="SELECT * FORM users")
        self.assertEqual(context.exception.get_position(), 9)

"""
9. Solution: Singleton Database Connection
"""
class Singleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(metaclass=Singleton):
    def __init__(self):
        self.connected = False
    
    def connect(self):
        if not self.connected:
            self.connected = True
            return True
        return False
    
    def disconnect(self):
        if self.connected:
            self.connected = False
            return True
        return False
    
    def execute_query(self, query):
        if self.connected:
            return "Query executed"
        raise ConnectionError("Not connected to database")

class TestSingleton(unittest.TestCase):
    def test_singleton(self):
        db1 = DatabaseConnection()
        db2 = DatabaseConnection()
        self.assertIs(db1, db2)
        
        self.assertTrue(db1.connect())
        self.assertEqual(db1.execute_query("SELECT * FROM users"), "Query executed")
        self.assertTrue(db1.disconnect())

"""
10. Solution: Plugin System
"""
class PluginMeta(type):
    plugins = {}
    
    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)
        if name != "Plugin":  # Don't register the base class
            cls.plugins[name] = new_cls
        return new_cls

class Plugin(metaclass=PluginMeta):
    @classmethod
    def is_compatible(cls):
        return True
    
    def execute(self):
        pass

class PluginLoader:
    @classmethod
    def get_available_plugins(cls):
        return list(PluginMeta.plugins.keys())
    
    @classmethod
    def load_plugin(cls, plugin_name):
        plugin_cls = PluginMeta.plugins.get(plugin_name)
        if plugin_cls:
            return plugin_cls()
        raise ValueError(f"Plugin {plugin_name} not found")

# Example plugins
class AudioPlugin(Plugin):
    def execute(self):
        return "Processing audio..."

class VideoPlugin(Plugin):
    def execute(self):
        return "Processing video..."

class TestPluginSystem(unittest.TestCase):
    def test_plugin_system(self):
        loader = PluginLoader()
        self.assertEqual(len(loader.get_available_plugins()), 2)
        
        audio_plugin = loader.load_plugin("AudioPlugin")
        self.assertIsInstance(audio_plugin, AudioPlugin)
        
        video_plugin = loader.load_plugin("VideoPlugin")
        self.assertTrue(video_plugin.is_compatible())


if __name__ == "__main__":
    unittest.main()
