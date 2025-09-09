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
