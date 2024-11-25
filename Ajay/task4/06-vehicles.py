from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def fuel_up(self, amount ):
        pass


class Car(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine_running = False
        self.fuel_level = 0
    
    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            print(f"The {self.make} {self.model}'s engine has started.")
        else:
            print(f"The {self.make} {self.model}'s engine is already running.")
    
    def stop_engine(self):
        if self.engine_running:
            self.engine_running = False
            print(f"The {self.make} {self.model}'s engine has stopped.")
        else:
            print(f"The {self.make} {self.model}'s engine is already stopped.")
    
    def fuel_up(self, amount):
        self.fuel_level += amount
        print(f"The {self.make} {self.model} has been fueled with {amount} liters. Current fuel level: {self.fuel_level} liters.")


class Motorcycle(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine_running = False
        self.fuel_level = 0
    
    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            print(f"The {self.make} {self.model}'s engine has started.")
        else:
            print(f"The {self.make} {self.model}'s engine is already running.")
    
    def stop_engine(self):
        if self.engine_running:
            self.engine_running = False
            print(f"The {self.make} {self.model}'s engine has stopped.")
        else:
            print(f"The {self.make} {self.model}'s engine is already stopped.")
    
    def fuel_up(self, amount):
        self.fuel_level += amount
        print(f"The {self.make} {self.model} has been fueled with {amount} liters. Current fuel level: {self.fuel_level} liters.")


class Truck(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine_running = False
        self.fuel_level = 0
    
    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            print(f"The {self.make} {self.model}'s engine has started.")
        else:
            print(f"The {self.make} {self.model}'s engine is already running.")
    
    def stop_engine(self):
        if self.engine_running:
            self.engine_running = False
            print(f"The {self.make} {self.model}'s engine has stopped.")
        else:
            print(f"The {self.make} {self.model}'s engine is already stopped.")
    
    def fuel_up(self, amount):
        self.fuel_level += amount
        print(f"The {self.make} {self.model} has been fueled with {amount} liters. Current fuel level: {self.fuel_level} liters.")


car = Car("Toyota", "Foruner")
motorcycle = Motorcycle("Royal Enfield", "Himalayan")
truck = Truck("Bharat Benz", "3528C")

car.start_engine()
motorcycle.start_engine()
truck.start_engine()

car.fuel_up(20)
motorcycle.fuel_up(10)
truck.fuel_up(50)

car.stop_engine()
motorcycle.stop_engine()
truck.stop_engine()
