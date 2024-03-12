#!/usr/bin/python3
"""Module for Square class, inherits from Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that defines a square by extending Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance.

        Inherits from Rectangle with equal width and height (size).
        Parameters:
            size: Edge length of the square.
            x: Horizontal position.
            y: Vertical position.
            id: Object identifier.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Property to get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Property setter to update the square's size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates attributes of the Square instance.

        Sequentially applies positional arguments or key/value pairs.
        Positional arguments must follow the order: id, size, x, y.
        Key/value pairs can be in any order.
        """
        if args and len(args) != 0:
            attributes = ['id', 'size', 'x', 'y']
            for a, arg in enumerate(args):
                if a < len(attributes):
                    setattr(self, attributes[a], arg)

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    def __str__(self):
        """String representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size)
