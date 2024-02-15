#!/usr/bin/python3
""" Square module. """


class Square():
    """ Square class. """
    width = 0
    height = 0

    def _init_(self, *args, **kwargs):
        """ Square class initialized """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Permiter of the square """
        return (self.width * 2) + (self.height * 2)

    def _str_(self):
        """ String representation of the square instance """
        return "{}/{}".format(self.width, self.height)


if _name_ == "_main_":
    """ Create Square instance """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
