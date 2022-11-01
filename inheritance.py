class Car:
    brand = ""
    model = ""
    year = 0
    speed = 0
    mileage = 0

    def __init__(self, brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

class ElectricCar(Car):
    batteryCapacity = 0

    # Constructor
    def __init__(self, brand, model, year, batteryCapacity):
        super().__init__(brand, model, year)
        self.batteryCapacity = batteryCapacity

class CEngineCar(Car):
    engineCapacity = 0

car = Car("Corola","Model S",2022)
car.year = 2020

electricCar = ElectricCar("Corola","Model S",2022, 2000)
# electricCar.batteryCapacity =2000

cEngineCar = CEngineCar("Corola","Model S",2022)
cEngineCar.brand = "Toyota"

print(f"Engine car model {cEngineCar.brand} and {car.year} is the year of the car")
print(f"{electricCar.batteryCapacity}")

class Toyota():
    newVariable = 0

newClass = Toyota()
newClass.batteryCapacity = 0
newClass.brand = "Merceedes"
