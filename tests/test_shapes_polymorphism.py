import math
from shapes.circle import Circle
from shapes.triangle import Triangle

def test_shapes_area_polymorphism():
    shapes = [
        Circle(1),            # π * 1^2 = 3.14159...
        Triangle(3, 4, 5),    # площадь = 6
    ]

    areas = [shape.area() for shape in shapes]

    assert math.isclose(areas[0], math.pi, rel_tol=1e-9)
    assert math.isclose(areas[1], 6.0, rel_tol=1e-9)
