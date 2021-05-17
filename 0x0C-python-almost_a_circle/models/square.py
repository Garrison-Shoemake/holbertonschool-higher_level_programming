#!/usr/bin/python3
""" This is the Square class, derived from Rectangle """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ This Class is a Square class, reminding us that a
    square is just a rectangle with equal sides """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """ string override """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size)
