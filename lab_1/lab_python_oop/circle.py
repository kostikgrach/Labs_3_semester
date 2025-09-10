from math import pi

from lab_python_oop.color import Color
from lab_python_oop.figure import Figure


class Circle(Figure):
    FIGURE_TYPE = 'Круг'

    @classmethod
    def get_figure_type(cls):
        return super().get_figure_type()

    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}'.format(
            Circle.get_figure_type(),
            self.color,
            self.radius,
            self.calculate_area()
        )
