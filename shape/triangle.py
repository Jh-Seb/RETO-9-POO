import math
from .base_shape import Shape, measure_time
from .point import Point
from .line import Line

class Triangle(Shape):
    def __init__(self, base=0, height=0, side1=0, side2=0, side3=0):
        super().__init__(is_regular=False)
        self._base = base
        self._height = height
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

        self.define_shape_type("Triangle")

        self.vertices = self.compute_vertices()
        self.edges = self.compute_edges()

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        self._base = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def side1(self):
        return self._side1

    @side1.setter
    def side1(self, value):
        self._side1 = value

    @property
    def side2(self):
        return self._side2

    @side2.setter
    def side2(self, value):
        self._side2 = value

    @property
    def side3(self):
        return self._side3

    @side3.setter
    def side3(self, value):
        self._side3 = value

    @measure_time
    def compute_area(self):
        return 0.5 * self._base * self._height

    def compute_perimeter(self):
        return self._side1 + self._side2 + self._side3

    def compute_vertices(self):
        return [
            Point(0, 0),
            Point(self._base, 0),
            Point(self._base / 2, self._height)
        ]

    def compute_edges(self):
        verts = self.compute_vertices()
        edges = []
        for i in range(3):
            edges.append(Line(verts[i], verts[(i + 1) % 3]))
        return edges

    def compute_inner_angles(self):
        a, b, c = self._side1, self._side2, self._side3
        if a == 0 or b == 0 or c == 0:
            return [0, 0, 0]

        angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        angle_C = 180 - angle_A - angle_B
        return [angle_A, angle_B, angle_C]
