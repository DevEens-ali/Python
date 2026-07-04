class Car:
    total_car = 0
    def __init__(self,brand,model,color):
        self.__brand = brand
        self.__model = model
        self.color = color
        Car.total_car+=1

    def get_brand(self):
        return self.__brand + "!!"
    
    def set_brand(self, __brand):
        self.__brand = __brand

    def fullName(self):
        return f"{self.__brand} {self.__model} {self.color}"
    
    def fuel_type(self):
        return "Water"

    @staticmethod
    def Car_description():
        return "Car is means for tranporting ...."
    
    @property #property decorator apply krnay k bad method as a attribute ki trah treat kiya jata hey
    def car_model(self):
        return self.__model


class Lambhorghini(Car):
    def __init__(self, brand, model, color,Petrol_tank):
        super().__init__(brand, model, color)
        self.Petrol_tank = Petrol_tank
    
    def fuel_type(self):
        return "Petrol deisal"


my_car = Car("BMW","M5","Blackish")
# my_car.car_model = "M7"
# print(my_car.car_model)



# print(my_car.Car_description())
# print(Car.Car_description())

# my_car1 = Car("Lambhorhini","SVJ","white")
# print(my_car.fuel_type())



lambhorhini = Lambhorghini("Lambhorhini","Aventador","SVJ","100Litre")
# lambhorhini = Lambhorghini("Ferrari","Aventador","SVJ","100Litre")
# print(isinstance(lambhorhini,Car))
# print(isinstance(lambhorhini,Lambhorghini))

# print(lambhorhini.Petrol_tank)
# print(lambhorhini.fullName())
# print(lambhorhini.fuel_type())
# print(Car.total_car)

# print(lambhorhini.__brand)

# print(my_car.brand)
# print(my_car.model)
# print(my_car.color)
# print(my_car.fullName())
# print(my_car1.brand)
# print(my_car1.model)
# print(my_car1.color)
# print(my_car1.fullName())


class Battery:
    def battery(self):
        return "Battery mathod"

class Engine:
    def engine(self):
        return "Engine"
class Electric_Car2(Battery,Engine,Car):
    pass
    
my_new_car = Electric_Car2("Tesla","model S","Black")
# print(my_new_car.battery())
# print(my_new_car.engine())

from abc import ABC, abstractmethod
class Enforce(ABC):
    @abstractmethod
    def engine_start(self):
        pass
    
class Bike(Enforce):
    def engine_start(self):
        return "Bike Start"
class Car(Enforce):
    def engine_start(self):
        return "Car Start"
class Truck(Enforce):
    def engine_start(self):
        return "truck Start"
bike = Bike()
car = Car()
truck = Truck() 

print(bike.engine_start())
print(car.engine_start())
print(truck.engine_start())