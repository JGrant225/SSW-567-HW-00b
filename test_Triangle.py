import unittest
from Triangle import Triangle

class TestTriangle(unittest.TestCase):
    def test_init(self):
        t = Triangle(3,4,5)
        self.assertEqual(t.a, 3)
        self.assertEqual(t.b, 4)
        self.assertEqual(t.c, 5)

    def test_equilateral(self):
        self.assertEqual(Triangle(3, 3, 3).classify(), "Equilateral")
        self.assertEqual(Triangle(100, 100, 100).classify(), "Equilateral")

    def test_isosceles(self):
        self.assertEqual(Triangle(3, 3, 2).classify(), "Isosceles")
        self.assertEqual(Triangle(2, 3, 3).classify(), "Isosceles")
        self.assertEqual(Triangle(5, 2, 5).classify(), "Isosceles")
        self.assertEqual(Triangle(100, 100, 50).classify(), "Isosceles")
        self.assertEqual(Triangle(50, 100, 100).classify(), "Isosceles")

    def test_scalene(self):
        self.assertEqual(Triangle(3, 4, 5).classify(), "Scalene")
        self.assertEqual(Triangle(5, 4, 3).classify(), "Scalene")
        self.assertEqual(Triangle(4, 5, 3).classify(), "Scalene")
        self.assertEqual(Triangle(7, 10, 12).classify(), "Scalene")

    def test_not_a_triangle(self):
        self.assertEqual(Triangle(1, 2, 3).classify(), "NotATriangle")
        self.assertEqual(Triangle(1, 10, 12).classify(), "NotATriangle")
        self.assertEqual(Triangle(51, 1, 10).classify(), "NotATriangle")
        self.assertEqual(Triangle(1, 10, 12).classify(), "NotATriangle")
        self.assertEqual(Triangle(51, 1, 10).classify(), "NotATriangle")

    def test_invalid_input(self):
        self.assertEqual(Triangle(-1, 2, 3).classify(), "InvalidInput")
        self.assertEqual(Triangle(1, -2, 3).classify(), "InvalidInput")
        self.assertEqual(Triangle(1, 2, -3).classify(), "InvalidInput")
        self.assertEqual(Triangle(0, 2, 3).classify(), "InvalidInput")
        self.assertEqual(Triangle(1, 0, 3).classify(), "InvalidInput")
        self.assertEqual(Triangle(1, 2, 0).classify(), "InvalidInput")

    def test_floats(self):
        self.assertEqual(Triangle(2.5, 2.5, 2.5).classify(), "Equilateral")
        self.assertEqual(Triangle(3.5, 3.5, 5.0).classify(), "Isosceles")
        self.assertEqual(Triangle(6.1, 7.2, 10.3).classify(), "Scalene")

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)