## Encapsulation

class Car:
    """A class to represent a car."""

    def __init__(self, make, model):
        self.make = make  # public attribute
        self._model = model  # protected attribute

    def display_info(self):
        print(f"Car: {self.make}, Model: {self._model}")

# Create an instance of Car
car = Car("Toyota", "Corolla")
car.display_info()  # Accessing public and protected attributes