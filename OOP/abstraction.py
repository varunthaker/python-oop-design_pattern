
from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    
class Car(vehicle):
    def start(self):
        return "Car started"
    def stop(self):
        return "Car stopped"

class Motorcycle(vehicle):
    def start(self):
        return "Motorcycle started"
    def stop(self): 
        return "Motorcycle stopped"


car1 = Car()
motorcycle1 = Motorcycle()

print(car1.start())
print(motorcycle1.start())

print(car1.stop())
print(motorcycle1.stop())

# use cases for abstraction
# 1. hiding the implementation details of a class
# 2. showing the essential features of a class
