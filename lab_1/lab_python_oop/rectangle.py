from lab_python_oop.figure import Figure
from lab_python_oop.color import Color


class Rectangle(Figure):
    FIGURE_TYPE = 'Прямоугольник'

    @classmethod
    def get_figure_type(cls):
        return super().get_figure_type()

    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def __repr__(self):
        return '{} {} цвета со сторонами {} и {} площадью {}'.format(
            Rectangle.get_figure_type(),
            self.color,
            self.width,
            self.height,
            self.calculate_area()
        )
