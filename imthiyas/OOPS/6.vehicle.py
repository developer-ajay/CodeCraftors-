"""
6. Medium: Create an abstract base class 'Vehicle' and implement concrete classes 
'Car', 'Motorcycle', and 'Truck'. Each should implement required methods:
- start_engine()
- stop_engine()
- fuel_up(amount)
Each vehicle type should have different fuel capacity and consumption rates.
"""
import unittest
import math
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


if __name__ == '__main__':
    unittest.main()
