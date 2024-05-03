class Vehicle:
    def __init__(self, engine_type, horsepower):
        self.engine_type = engine_type
        self.horsepower = horsepower

    def print_praise_for_engine_type(self):
        if (self.engine_type == "electric"):
            print("Nice, you are a good person to climate change!")
        elif (self.engine_type == "hybrid"):
            print("Ok, you are trying.")
        elif (self.engine_type == "fuel"):
            print("Ok, still ok, but maybe you need an upgrade in the future.")
        else:
            print("Invalid engine_type", self.engine_type)
            
class Car(Vehicle):
    def __init__(self, engine_type, horsepower, people_count):
        super().__init__(engine_type, horsepower)
        self.people_count = people_count

    def calculate_power_per_person(self):
        return self.horsepower / self.people_count

class Truck(Vehicle):
    def __init__(self, engine_type, horsepower, max_tonnage):
        super().__init__(engine_type, horsepower)
        self.max_tonnage = max_tonnage

    def calculate_power_per_ton(self):
        return self.horsepower / self.max_tonnage

def main():
    print("Car")
    car = Car("fuel", 220, 5)
    car.print_praise_for_engine_type()
    print(car.calculate_power_per_person())

    print()

    print("Truck")
    truck = Truck("hybrid", 642, 25)
    truck.print_praise_for_engine_type()
    print(truck.calculate_power_per_ton())

if __name__ == "__main__":
    main();
