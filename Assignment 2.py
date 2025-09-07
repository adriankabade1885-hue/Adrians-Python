"R244530h"
"Base class vehicle"
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        def display(self):
            print("Make:", self.make, "Model:", self.model, "Year:", self.year)

            'Sublclass car'
            class Car(Vehicle):
                def __init__(self, make, model, year, num_doors):
                    super().__init__(brand, model)
                    self.num_doors = num_doors
                    def display_details(self):
                        super().display_details()
                        print("Number of doors:", self.num_doors)
                        "Sublclass bike"
                        class Bike(Vehicle):
                            def __init__(self, make, model, year, engine_capacity):
                                super().__(brand, model)
                                self.engine_capacity = engine_capacity
                                def display_details(self):
                                    super().display_details()
                                    print(f"engine_capacity: {self.engine_capacity}cc")
                                    "Question 2"
                                    import math

                                    # Base class for Shape
                                    class Shape:
                                        def area(self):
                                            raise NotImplementedError("Subclass must implement abstract method")

                                    # Circle class inheriting from Shape
                                    class Circle(Shape):
                                        def __init__(self, radius):
                                            self.radius = radius

                                        def area(self):
                                            return math.pi * (self.radius ** 2)

                                    # Rectangle class inheriting from Shape
                                    class Rectangle(Shape):
                                        def __init__(self, width, height):
                                            self.width = width
                                            self.height = height

                                        def area(self):
                                            return self.width * self.height

                                    # Function to calculate total area of shapes
                                    def total_area(shapes):
                                        total = 0
                                        for shape in shapes:
                                            total += shape.area()
                                        return total

                                    # Example usage
                                    shapes = [Circle(8), Rectangle(7, 6), Circle(3)]
                                    print("Total area of shapes:", total_area(shapes))
"question 3"
Base class Shape
class Shape:
    def _init_(self, color):
        self.color = color

    def calculate_area(self):
        pass


class Rectangle(Shape):
    def _init_(self, color, width, height):
        super()._init_(color)  # Call Shape's constructor
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

"an example interpreting how this code would work"
rectangle = Rectangle("beige", 7, 6)
print(f"Color: {rectangle.color}")
print(f"Area: {rectangle.calculate_area()}")


"question 4"
"function to process animal sounds between dog and cat"
def process_sound(sound_object):
    sound_object.make_sound()

# Dog class
class Dog:
    def make_sound(self):
        print("hoo hoo!")

# Cat class
class Cat:
    def make_sound(self):
        print("Meow!")

# Example usage
dog = Dog()
cat = Cat()

print("Dog's sound:")
process_sound(dog)

print("Cat's sound:")
process_sound(cat)

"question 5"
"base class"
from abc import ABC, abstractmethod
class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

"TextFileHandler "
class TextFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            return file.read()

    def write(self, data):
        with open(self.filename, 'w') as file:
            file.write(data)

"BinaryFileHandler"
class BinaryFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'rb') as file:
            return file.read()

    def write(self, data):
        with open(self.filename, 'wb') as file:
            file.write(data)