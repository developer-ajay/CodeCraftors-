
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
    pass

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

class Truck(Vehicle):
    pass

class TestVehicles(unittest.TestCase):
    def test_vehicles(self):
        car = Car()
        self.assertTrue(car.start_engine())
        self.assertEqual(car.fuel_up(50), "Fueled up 45L. Tank full.")
        self.assertTrue(car.stop_engine())
        
        motorcycle = Motorcycle()
        self.assertEqual(motorcycle.fuel_up(20), "Fueled up 15L. Tank full.")
        
        truck = Truck()
        self.assertEqual(truck.fuel_up(200), "Fueled up 200L")

if __name__ == '__main__':
    unittest.main()
