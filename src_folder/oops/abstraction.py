## Abstraction

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract class for shapes."""

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(f"Area of the circle: {circle.area()}")