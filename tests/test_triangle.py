import math
import pytest
from shapes.triangle import Triangle

def test_triangle_area():
    triangle = Triangle(3, 4, 5)
    assert math.isclose(triangle.area(), 6.0, rel_tol=1e-9)

def test_triangle_invalid_sides():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)  # невозможный треугольник

def test_triangle_is_right():
    triangle = Triangle(3, 4, 5)
    assert triangle.is_right() is True

def test_triangle_not_right():
    triangle = Triangle(3, 3, 3)
    assert triangle.is_right() is False
