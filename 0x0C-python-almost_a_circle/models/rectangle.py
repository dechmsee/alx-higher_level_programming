#!/usr/bin/python3
"""Module that contains a rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Class that represents a rectangle"""

    def __init__(self,width, height, x=0, y=0, id=None):
        """Initialises the object attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # List of the getter functions
    @property
    def width(self):
        """Gets the value for width"""
        return self._width

    @property
    def height(self):
        """Gets the value for height"""
        return self._height

    @property
    def x(self):
        """Gets the value for x"""
        return self._x

    @property
    def y(self):
        """Gets the value for y"""
        return self._y
    
    # List of setter functions
    @width.setter
    def width(self, value):
        """Sets the value for width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        
        self._width = value

    @height.setter
    def height(self, value):
        """Sets the value for height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        
        if value <= 0:
            raise ValueError("height must be > 0")
        self._height = value

    @x.setter
    def x(self, value):
        """Sets the value for x"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        
        if value <= 0:
            raise ValueError("x must be >= 0")
        self._x = value

    @y.setter
    def y(self, value):
        """Sets the value for y"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")
            
        if value <= 0:
            raise ValueError("y must be > 0")
        self._y = value
