from math import pi

from lab_python_oop.color import Color
from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    FIGURE_TYPE = 'Квадрат'

    @classmethod
    def get_figure_type(cls):
        return super().get_figure_type()

    def __init__(self, size, color):
        super().__init__(size, size, color)

    def calculate_area(self):
        return super().calculate_area()

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}'.format(
            Square.get_figure_type(),
            self.color,
            self.height,
            self.calculate_area()
        )
