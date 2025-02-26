class Car:
    def __init__(self, brand:str, model:str):
        self.brand = brand
        self.model = model

    def car_info(self):
        return f"Brand: {self.brand}, Modal: {self.model}"


# Inheritance
class ElectricCar(Car):
    battery_size:int

    def __init__(self, brand:str, model:str, battery_size:int):
        # Call the constructor of the parent class
        super().__init__(brand, model)
        self.battery_size = battery_size

    # Override the method of the parent class
    # this will be called first and if not than the method of the parent class will be called
    def car_info(self):
        return f"Brand: {self.brand}, Modal: {self.model}, Battery Size: {self.battery_size}"


ele_car = ElectricCar("Tesla", "Model S", 25)

print(ele_car.car_info())
