import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds.")
        return result
    return wrapper

class Shape:
    shape_type = "Generic"

    def __init__(self, is_regular=False, vertices=None, edges=None, inner_angles=None):
        self._is_regular = is_regular
        self._vertices = vertices if vertices else []
        self._edges = edges if edges else []
        self._inner_angles = inner_angles if inner_angles else []


    @property
    def is_regular(self):
        return self._is_regular

    @is_regular.setter
    def is_regular(self, value):
        self._is_regular = value

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, value):
        self._vertices = value

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, value):
        self._edges = value

    @property
    def inner_angles(self):
        return self._inner_angles

    @inner_angles.setter
    def inner_angles(self, value):
        self._inner_angles = value

    @classmethod
    def define_shape_type(cls, new_type):
        cls.shape_type = new_type

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass

    def compute_inner_angles(self):
        pass
