#!/usr/bin/python3
""" This is the Rectangle Class, derived from Base """


from models.base import Base


class Rectangle(Base):
    """ This is the Rectangle subclass, derived from Base
    should also have unique ids, as per Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns area """
        return self.height * self.width

    def display(self):
        """ prints the rectangle """
        for i in range(self.y):
            print('\n', end="")
        for i in range(self.__height):
            for i in range(self.x):
                print(' ', end="")
            for i in range(self.__width):
                    print('#', end="")
            print()

    def __str__(self):
        """ str override """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """ this function updates information given
        based on arguments given by user """
        ids = ['id', 'width', 'height', 'x', 'y']
        i = 0
        if args:
            for arg in args:
                setattr(self, ids[i], args[i])
                i += 1
        if kwargs:
            for arg in kwargs:
                setattr(self, arg, kwargs[arg])
