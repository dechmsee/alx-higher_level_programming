#!/usr/bin/python3
# 2-square.py by Dennis Mutui
"""A module that defines a square"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Creates a square
        Args:
            size: length of the square side
            position: where square is (coordinates)
        """
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """Property of size as the len of the side of a square
        Raises:
        TypeError: if size != int
        ValueError: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    @property
    def position(self):
        """property of the coordinates of this square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of square
        Args: value as a tuple of 2 positive integers
        Raises:
            TypeError: if value is not a tuple or any int in tuple < 0
            """

        if not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """
        Calculate area of square
        Returns: The square of the size
        """

        return self.__size ** 2

    def my_print(self):
        """prints the sqaure in # """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)

    def pos_print(self):

        pos = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """print the square in position"""
        print(self.pos_print(), end='')
