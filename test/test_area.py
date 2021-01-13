import unittest
import sys

# sys.path.append('../')
from src.area import Area


class AreaTest(unittest.TestCase):

    def test_square_area_side_positive(self):
        self.assertEquals(Area.square(8), 64)

    def test_square_area_side_negative(self):
        self.assertEquals(Area.square(-5), 0)

    def test_square_area_side_zero(self):
        self.assertEquals(Area.square(0), 0)

    def test_square_area_side_large_number(self):
        self.assertEquals(Area.square(12345678), 152415765279684)

    def test_rectangle_area_valid_numbers(self):
        self.assertEquals(Area.rectangle(5, 6), 30)