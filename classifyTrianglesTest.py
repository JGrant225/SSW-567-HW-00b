import unittest
from classifyTriangles import classifyTriangles
class TestClassifyTriangles(unittest.TestCase):
    def test_init(self):
        t = classifyTriangles(3,4,5)
        self.assertEqual(t.a, 3)
        self.assertEqual(t.b, 4)
        self.assertEqual(t.c, 5)

    def test_equilateral(self):
        self.assertEqual(classifyTriangles(3, 3, 3).classifyTriangle(), "Equilateral")

    def test_isosceles(self):
        self.assertEqual(classifyTriangles(3, 3, 2).classifyTriangle(), "Isosceles")
        self.assertEqual(classifyTriangles(2, 3, 3).classifyTriangle(), "Isosceles")
        self.assertEqual(classifyTriangles(5, 2, 5).classifyTriangle(), "Isosceles")

    def test_scalene(self):
        self.assertEqual(classifyTriangles(3, 4, 5).classifyTriangle(), "Scalene")
        self.assertEqual(classifyTriangles(5, 4, 3).classifyTriangle(), "Scalene")
        self.assertEqual(classifyTriangles(4, 5, 3).classifyTriangle(), "Scalene")

    def test_not_a_triangle(self):
        self.assertEqual(classifyTriangles(1, 2, 3).classifyTriangle(), "NotATriangle")
        self.assertEqual(classifyTriangles(1, 10, 12).classifyTriangle(), "NotATriangle")
        self.assertEqual(classifyTriangles(51, 1, 10).classifyTriangle(), "NotATriangle")

    def test_invalid_input(self):
        self.assertEqual(classifyTriangles(-1, 2, 3).classifyTriangle(), "InvalidInput")
        self.assertEqual(classifyTriangles(1, -2, 3).classifyTriangle(), "InvalidInput")
        self.assertEqual(classifyTriangles(1, 2, -3).classifyTriangle(), "InvalidInput")
        self.assertEqual(classifyTriangles(0, 2, 3).classifyTriangle(), "InvalidInput")
        self.assertEqual(classifyTriangles(1, 0, 3).classifyTriangle(), "InvalidInput")
        self.assertEqual(classifyTriangles(1, 2, 0).classifyTriangle(), "InvalidInput")

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)