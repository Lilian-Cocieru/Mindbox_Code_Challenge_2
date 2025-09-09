from shapes.circle import Circle
from shapes.triangle import Triangle

def main():
    circle = Circle(5)
    print("Circle area:", circle.area())

    triangle = Triangle(3, 4, 5)
    print("Triangle area:", triangle.area())
    print("Is right triangle:", triangle.is_right())

if __name__ == "__main__":
    main()



# from abc import ABC, abstractmethod
# from math import sqrt, pi


# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         if radius < 0:
#             raise ValueError("The radius cannon be negative.")
#         self.radius = radius
    
#     def area(self):
#         return pi * self.radius ** 2

# class Triangle(Shape):
#     def __init__(self, side1, side2, side3):
#         sides = sorted([side1, side2, side3])
#         if sides[0] + sides[1] <= sides[2]:
#             raise ValueError("This is not a triangle.")
#         self.sides = sides
#     def area(self):
#         a, b, c = self.sides
#         s = (a + b + c) / 2
#         return sqrt(s * (s - a) * (s - b) * (s - c))
#     def is_right_triangle(self):
#         a, b, c = self.sides
#         return a ** 2 + b ** 2 == c ** 2

# # Usage
# circle = Circle(5)
# triangle = Triangle(3, 4, 5)

# shapes = [circle, triangle]
# for shape in shapes:
#     print(f"Area: {shape.area()}")
