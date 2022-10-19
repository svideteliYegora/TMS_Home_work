'''
Написать класс, который будет создавать треугольник по трём его сторонам.
В класс добавить метод, проверяющий возможность построения данного треугольника.
Добавить свойства треугольника (длины его сторон) с помощью @ property.
'''

class CreateTringle:

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # getter and setter for all sides
    @property
    def sides(self):
        return self._a, self._b, self._c

    @sides.setter
    def sides(self, kort: tuple):
        print('Setter worked.')
        self._a = kort[0]
        self._b = kort[1]
        self._c = kort[2]

    # getter and setter for everyone side
    @property
    def a(self):
        return self._a
    @a.setter
    def a(self, a: float):
        print('Setter worked.')
        self._a = a

    @property
    def b(self):
        return self._b
    @b.setter
    def b(self, b: float):
        print('Setter worked.')
        self._b = b

    @property
    def c(self):
        return self._c
    @c.setter
    def c(self, c: float):
        print('Setter worked.')
        self._c = c

    def check(self):
        if self._a + self._b > self._c and self._a + self._c > self._b and self._b + self._c > self._a:
            print(f"Triangle with sides: {self._a}, {self._b}, {self._c} exists!")
        else:
            print(f"Triangle with sides: {self._a}, {self._b}, {self._c} not exists!")

triangle = CreateTringle(a=5, b=6, c=7)
triangle.c = 2
print(triangle.sides)
triangle.sides = 4, 8, 9
print(triangle.sides)
triangle.check()
