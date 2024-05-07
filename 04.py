import math


class GeometricObject:
    def __init__(self, x=0.0, y=0.0, color='black', filled=False):
        self.__x = float(x)
        self.__y = float(y)
        self.color = color
        self.filled = filled

    def set_coordinate(self, x, y):
        if isinstance(x, int):
            if isinstance(y, int):
                self.__x = float(x)
                self.__y = float(y)

    def set_color(self, color):
        self.color = color

    def set_filled(self, filled):
        self.filled = filled

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_color(self):
        return self.color

    def is_filled(self):
        return self.filled

    def __str__(self):
        return f"({self.__x},{self.__y})\n" + f"color: {self.color}\nfilled: {self.filled}"

    def __repr__(self):
        if self.filled is True:
            return f"({int(self.__x)},{int(self.__y)}) " + f"{self.color} filled"
        else:
            return f"({int(self.__x)},{int(self.__y)}) " + f"{self.color} no filled"


class Circle(GeometricObject):
    def __init__(self, x=0.0, y=0.0, radius=0.0, color='black', filled=False):
        super().__init__(x, y, color, filled)
        if radius >= 0:
            self.__radius = radius
        else:
            self.__radius = 0.0

    @property
    def radius(self):
        if self.__radius >= 0:
            return self.__radius
        else:
            self.__radius = 0.0
            return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius >= 0:
            self.__radius = float(radius)
        else:
            self.__radius = 0.0

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_perimetr(self):
        return 2 * self.__radius * math.pi

    def get_diametr(self):
        return 2 * self.__radius

    def __str__(self):
        return f"radius: {self.__radius}\n" + super().__str__()

    def __repr__(self):
        return f"radius:{int(self.__radius)} " + super().__repr__()


class Rectangle(GeometricObject):
    def __init__(self, x=0.0, y=0.0, width=0.0, height=0.0, color='black', filled=False):
        super().__init__(x, y, color, filled)
        if width >= 0:
            self.width = width
        else:
            self.width = 0.0
        if height >= 0:
            self.height = height
        else:
            self.height = 0.0

    def set_width(self, width):
        if isinstance(width, int):
            if width >= 0:
                self.width = float(width)

    def set_height(self, height):
        if isinstance(height, int):
            if height >= 0:
                self.height = float(height)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.height * self.width

    def get_perimetr(self):
        return 2 * (self.height + self.width)

    def is_filled(self):
        return self.filled

    def __str__(self):
        return f"width: {self.width}\n" + f"height: {self.height}\n" + super().__str__()

    def __repr__(self):
        return f"width: {int(self.width)} " + f'height:{int(self.height)} ' + super().__repr__()


point = GeometricObject()
print(point)
print()
point.set_coordinate(-4, 9)
print(point.get_x())
print(point.get_y())
point.set_color('red')
print(point.get_color())
point.set_filled(True)
print(point.is_filled())
print()
print(point)
print()
point_2 = GeometricObject(8, -4, 'blue', True)
print(point_2)
print()
circle = Circle()
print(circle)
print()
circle.radius = -34
print(circle.radius)
circle.radius = 12
print(circle.radius)
print()
circle_2 = Circle(3, -100, 20, 'green', True)
print(circle_2)
print()
circle_2.set_color('grey')
print(circle_2.get_color())
print()
print(circle_2.get_area())
print(circle_2.get_perimetr())
print(circle_2.get_diametr())
print()
circle_3 = Circle(90, -84, -223, 'pink')
print(circle_3)
print()
rectangle = Rectangle()
print(rectangle)
print()
rectangle.set_coordinate(11, 29)
rectangle.set_color('yellow')
rectangle.set_width(-10)
rectangle.set_height(20)
print(rectangle)
print()
rectangle.set_width(100)
print(rectangle.get_width())
print(rectangle.get_height())
print()
print(rectangle.get_area())
print(rectangle.get_perimetr())
print()
rectangle_2 = Rectangle(10, 20, 30, -40, 'brown', True)
print(rectangle_2)
print()
figures = []
figures.append(point)
figures.append(circle_2)
figures.append(rectangle)
print(figures)
