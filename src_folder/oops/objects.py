## Objects

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car: {self.make}, Model: {self.model}, Year: {self.year}")

my_car = Car("Toyota", "Corolla", 2022)
my_second_car = Car("Honda", "Civic", 2023)  # Object creation for my_second_car
my_second_car.display_info()