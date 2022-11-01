#!/usr/bin/python3
"""Module that contains a class to serve as base for other classes"""


import json

class Base:
    """Base of all the classes created"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects
            Base.__nb_objects += 1
