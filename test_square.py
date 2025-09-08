import pytest
from square import get_square

def test_sq():
    x = 5
    res = get_square(x)
    assert res == 25
    assert get_square(3) == 9