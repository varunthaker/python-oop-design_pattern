class Car:
    def __init__(self, brand:str):
        self.brand = brand
    
    def fuel_type(self):
        return "petrol or Diesel"



class ElectricCar(Car):

    def __init__(self, brand:str):
        super().__init__(brand)
    
    def fuel_type(self):
        return "Electric"
    

car1 = Car("Toyota")
ele_car = ElectricCar("Tesla")

# Polymorphism
print(car1.fuel_type())
print(ele_car.fuel_type())


