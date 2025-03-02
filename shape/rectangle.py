from .base_shape import Shape, measure_time
from .point import Point
from .line import Line

class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        super().__init__(is_regular=True)
        self._width = width
        self._height = height
        self.define_shape_type("Rectangle") 


        self.vertices = self.compute_vertices()
        self.edges = self.compute_edges()

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @measure_time
    def compute_area(self):
        return self._width * self._height

    def compute_perimeter(self):
        return 2 * (self._width + self._height)

    def compute_vertices(self):
        return [
            Point(0, 0),
            Point(self._width, 0),
            Point(self._width, self._height),
            Point(0, self._height)
        ]

    def compute_inner_angles(self):
        return [90, 90, 90, 90]

    def compute_edges(self):
        verts = self.compute_vertices()
        edges = []
        for i in range(4):
            edges.append(Line(verts[i], verts[(i + 1) % 4]))
        return edges
