from abc import ABC, abstractmethod

# Abstract class for Shape
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape, Drawable):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.1416 * self.radius * self.radius

    def draw(self):
        print(f"Drawing a Circle with radius {self.radius}")

class Rectangle(Shape, Drawable):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def draw(self):
        print(f"Drawing a Rectangle of width {self.width} and height {self.height}")

circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Circle Area: {circle.calculate_area()}")
circle.draw()

print(f"Rectangle Area: {rectangle.calculate_area()}")
rectangle.draw()
