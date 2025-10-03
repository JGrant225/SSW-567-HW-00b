"""Module for classifying triangles by side lengths."""

class Triangle:
    """Represents a triangle and provides classification."""
    def __init__(self, a, b, c):
        """Initialize triangle with side lengths a, b, and c."""
        self.a = a
        self.b = b
        self.c = c

    def classify(self):
        """Classify the triangle as Equilateral, Isosceles, Scalene,
        NotATriangle, or InvalidInput.
        """
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "InvalidInput"
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return "NotATriangle"
        if self.a == self.b and self.b == self.c:
            return "Equilateral"
        if self.a == self.b or self.b == self.c or self.a == self.c:
            return "Isosceles"
        return "Scalene"
    