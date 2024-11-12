##  Inheritance

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def display_info(self):
        return f"Employee: {self.name}, Position: {self.position}"

class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name, "Manager")  # Call the parent class constructor
        self.department = department
    
    def display_info(self):
        return f"{super().display_info()}, Department: {self.department}"

class Developer(Employee):
    def __init__(self, name, programming_language):
        super().__init__(name, "Developer")  # Call the parent class constructor
        self.programming_language = programming_language
    
    def display_info(self):
        return f"{super().display_info()}, Programming Language: {self.programming_language}"

# Create instances of Manager and Developer
manager = Manager("Alice", "Sales")
developer = Developer("Bob", "Python")

print(manager.display_info())
print(developer.display_info())