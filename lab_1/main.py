import numpy as np

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.sqare import Square


if __name__ == '__main__':
    n = 7    #float(input('Введите N:'))
    print(Rectangle(n, n, 'синего'))
    print(Circle(n, 'зеленого'))
    print(Square(n, 'красного'))

    print(np.array([1, 2, 3]))
