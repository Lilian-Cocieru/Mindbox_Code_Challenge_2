import math
import pytest
from shapes.circle import Circle

def test_circle_area():
    circle = Circle(5)
    assert math.isclose(circle.area(), math.pi * 25, rel_tol=1e-9)

def test_circle_invalid_radius():
    with pytest.raises(ValueError):
        Circle(-3)
