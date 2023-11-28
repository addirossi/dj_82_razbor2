from django.test import TestCase

# Create your tests here.
import pytest


@pytest.mark.parametrize(
    'quantity, status_code', [
        (21, 400),
        (19, 200)
    ]
)
def test_add(x, y, z):
    assert x + y == z
