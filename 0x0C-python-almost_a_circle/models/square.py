#!/usr/bin/python3
"""This module contains a square class"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """A square class"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = id
        super().__init__(size, x, y, id)

    def __str__(self):
        """Defines a format for the string representation of the class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

