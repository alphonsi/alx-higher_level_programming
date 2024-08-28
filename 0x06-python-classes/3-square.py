#!/usr/bin/python3
<<<<<<< HEAD
"""Square module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Length of a side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Area of this square.

        Returns:
            The size squared.
        """
=======
""" defines a square """


class Square:
    """ square with private instance attribute size """

    def __init__(self, size=0):
        """
        initializes square

        Args:
            size: size of side of square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        finds area of square

        Returns:
            the area of the square
        """

>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
        return self.__size ** 2
