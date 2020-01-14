#!/usr/bin/python3
"""Rectangle module that defines a square"""
class Rectangle:
    """Class rectangle"""
    def __init__(self, width=0, height=0):
        """New instance initalization"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Gets the value width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value width"""
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")

    @property
    def height(self):
        """Gets the value height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value height"""
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")

    def area(self):
        """Area of a rectangle"""
        return self.__width*self.__height

    def perimeter(self):
        """Rectangle perimeter"""
        if self.__width is 0  or self.__height is 0:
            return 0
        else:
            return 2*(self.__width+self.__height)
