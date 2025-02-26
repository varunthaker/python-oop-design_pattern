# Class
class Car:
    # Attributes
    brand:str
    model:str


    # Constructor
    def __init__(self, brand:str, model:str):
        self.brand = brand
        self.model = model
    
    # Method
    def car_info(self):
        return f"Brand: {self.brand}, Modal: {self.model}"

# Object 1  instance of class Car
car1 = Car("Toyota", "Corolla")
car1_fullname = car1.car_info()

print(car1.brand)
print(car1.model)
print(car1_fullname)



