#!/usr/bin/python3
"""This module defines a class MyInt that inherits from int"""



class MyInt(int):
    """Inverts Int operators == and !="""

    def __eq__(self, value):
        """Overrides == operator with != behaviour"""
        return self.real != value
        
    def __ne__(self, value):
        """Overrides!= operator with == behaviour"""
        return self.real == value
