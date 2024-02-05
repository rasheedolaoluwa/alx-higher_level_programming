#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Inverts int equality and inequality operations."""

    def __eq__(self, value):
        """Inverts the == operator to perform as !=."""
        return self.real != value

    def __ne__(self, value):
        """Inverts the != operator to perform as ==."""
        return self.real == value
