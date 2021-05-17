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
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """ string override """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size)

    def update(self, *args, **kwargs):
        """ this updates similarly to rectangle """

        ids = ['id', 'size', 'x', 'y']
        i = 0
        if args:
            for arg in args:
                setattr(self, ids[i] args[i])
                i += 1
        if kwargs:
            for arg in kwargs:
                setattr(self, arg, kwargs[arg])
