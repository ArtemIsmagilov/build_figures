# from math import pi

pi = 3.14


def is_triangle(a, b, c) -> bool:
    """
    В невырожденном треугольнике сумма длин двух его сторон больше длины третьей стороны, в вырожденном — равна.
    >>> is_triangle(1, 2, 3)
    True
    >>> is_triangle(-1, 2, 4)
    False
    >>> is_triangle(1, 2, 99)
    False
    """
    return a >= 0 and b >= 0 and c >= 0 and a + b >= c and a + c >= b and b + c >= a


def is_right_rectangle(a, b, c) -> bool:
    """
    Прямоугольный треугольник
    >>> is_right_rectangle(1, 1, 2 ** 0.5)
    True
    >>> is_right_rectangle(10, 3, 290)
    False
    """
    AB, BC, AC = sorted((a, b, c))
    return round_by_ndigits_2(AB ** 2 + BC ** 2) == round_by_ndigits_2(AC ** 2)


def round_by_ndigits_2(number: float | int) -> float:
    return round(number, 2)


class ClientError(Exception):
    pass


class Figure:
    pass


class Triangle(Figure):
    def __init__(self, a, b, c):
        """
        >>> Triangle(-1, 2, 10)
        Traceback (innermost last):
        ClientError: A triangle with input a,b and c does not exist
        >>> Triangle(1, 2, 50)
        Traceback (innermost last):
        ClientError: A triangle with input a,b and c does not exist
        >>> Triangle(1, 50, 2)
        Traceback (innermost last):
        ClientError: A triangle with input a,b and c does not exist
        >>> Triangle(50, 1, 2)
        Traceback (innermost last):
        ClientError: A triangle with input a,b and c does not exist
        >>> triangle = Triangle(2, 3, 4)
        """
        if not is_triangle(a, b, c):
            raise ClientError('A triangle with input a,b and c does not exist')

        self.a = a
        self.b = b
        self.c = c

    def P(self) -> float | int:
        """
        >>> triangle = Triangle(1, 2, 3); triangle.P()
        6
        >>> triangle = Triangle(3, 4, 5); triangle.P()
        12
        >>> triangle = Triangle(40, 32, 50); triangle.P()
        122
        """
        return round_by_ndigits_2(self.a + self.b + self.c)

    def S(self) -> float | int:
        """
        >>> triangle = Triangle(1, 2, 3); triangle.S()
        0.0
        >>> triangle = Triangle(3, 4, 3); triangle.S()
        4.47
        >>> triangle = Triangle(40, 32, 50); triangle.S()
        639.25
        """
        p = round_by_ndigits_2(self.P() / 2)
        return round_by_ndigits_2((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5)


class Circle(Figure):
    def __init__(self, r: int):
        self.r = r

    def S(self) -> float | int:
        """
        >>> circle = Circle(1); circle.S()
        3.14
        >>> circle = Circle(3); circle.S()
        28.26
        >>> circle = Circle(54523); circle.S()
        9334458641.06
        """
        return round_by_ndigits_2(pi * (self.r ** 2))


class Rectangle(Figure):
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def S(self) -> float | int:
        """
        >>> rectangle = Rectangle(2, 4)
        >>> rectangle.S()
        8
        """
        return round_by_ndigits_2(self.a * self.b)

    def P(self) -> float | int:
        """
        >>> rectangle = Rectangle(2, 4)
        >>> rectangle.P()
        12
        """
        return round_by_ndigits_2(self.a * 2 + self.b * 2)


class Square(Figure):
    def __init__(self, a: int):
        self.a = a

    def P(self) -> float | int:
        """
        >>> square = Square(3)
        >>> square.P()
        12
        """
        return round_by_ndigits_2(self.a * 4)

    def S(self) -> float | int:
        """
        >>> square = Square(3)
        >>> square.S()
        9
        """
        return round_by_ndigits_2(self.a ** 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
