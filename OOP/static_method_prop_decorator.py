class Car:
    def __init__(self, brand:str):
        self.__brand = brand

    # static method
    # This is a method that is not bound to the class or instance
    @staticmethod
    def get_car_info():
        return "This is a car"
    
    # property decorator
    # This is a decorator that is used to get the value of a property
    @property
    def brand(self):
        return self.__brand
    
    
# can be called using the class name
print(Car.get_car_info())

# cant be called using the instance or object name
car1 = Car("Toyota")

# property decorator
print(car1.brand)

# property decorator does not allow to override the value
# car1.brand = "Ford"
# print(car1.brand)





# use cases for static methods
# utility functions that don't need to access instance or class data

# use cases for property decorator
# to get the value of a property
