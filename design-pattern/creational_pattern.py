from abc import ABC, abstractmethod

# Singleton Pattern
# only one instance of the class is created db1
# db1 can be used anywhere in the code/app

class Database:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
        
db1 = Database()
db2 = Database()

print(db1 is db2)


# Factory Pattern
# from schema factory, we can get the schema we want
# What comes in for specific schema comes from subclasses

class UserSchema(ABC):
  username: str
  email: str
  password: str

class ProductSchema(ABC):
  name: str
  price: float
  description: str

class SchemaFactory:
    @staticmethod
    def get_schema(schema_type: str):
        if schema_type == 'user':
            return UserSchema()
        elif schema_type == 'product':
            return ProductSchema()
        else:
            raise ValueError(f"Invalid schema type: {schema_type}")
    

print(SchemaFactory.get_schema('user'))

    
    
    
