## Polymorphism

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def make_sound(self, sound="Bark"):
        print(f"{self.name} says {sound}")

class Cat(Animal):
    def make_sound(self, sound="Meow"):
        print(f"{self.name} says {sound}")

# Polymorphism in action
animals = [Dog("Buddy"), Cat("Whiskers")]

for animal in animals:
    animal.make_sound()  # Calls the make_sound method based on the object type