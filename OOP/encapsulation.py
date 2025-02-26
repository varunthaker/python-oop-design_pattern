class Car:
    def __init__(self, brand:str, model:str):
        self.model = model
        # Private attribute
        self.__brand = brand

    def get_brand(self):
        return self.__brand
    
    def set_brand(self, brand:str):
        self.__brand = brand
    

car1 = Car("Toyota", "Corolla")

# Getting and setting public attributes
car1.model = "Tundra"
print(car1.model)

# Getting and setting private attributes
car1.set_brand("Ford")
print(car1.get_brand())

