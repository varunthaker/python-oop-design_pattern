class Car:
    # Class variable
    # This is shared by all instances of the class
    total_cars = 0
    
    def __init__(self, brand:str):
        self.brand = brand
        Car.total_cars += 1
    

class ElectricCar(Car):

    def __init__(self, brand:str):
        super().__init__(brand)
    

Car("Toyota")
Car("Ford")

# good practice
    # It should be accessed using the class name
print(Car.total_cars)

test = ElectricCar("Tesla")

# bad practice
# It should not be accessed using the instance or object name
print(test.total_cars)


# use cases for class variables
# 1. tracking the number of instances of a class (number of cars, number of employees)


