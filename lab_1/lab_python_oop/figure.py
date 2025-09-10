from abc import ABC, abstractmethod

from lab_python_oop.color import Color


class Figure(ABC):
    FIGURE_TYPE = 'Фигура'

    def __init__(self, color):
        super().__init__()
        self.color = Color(color)

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    @abstractmethod
    def calculate_area(self):
        pass
