#!/usr/bin/python3
<<<<<<< HEAD
"""Square module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Length of a side of the square.
        """
        self.size = size

    @property
    def size(self):
        """Property for the length of a side of this square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
=======


class Square:
    """
    creates square
    """

    def __init__(self, size=0):
        """
        initializes square

        Args:
            size: size of side of square
        """
        self.__size = size

    @property
    def size(self):
        """
        finds size
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
        """
        return self.__size

    @size.setter
    def size(self, value):
<<<<<<< HEAD
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of this square.

        Returns:
            The size squared.
=======
        """
        validates size is an integer that is greater than zero
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """
        finds area of square

        Returns:
            area of square
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
        """
        return self.__size ** 2

    def __eq__(self, other):
<<<<<<< HEAD
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
=======
        """
        check if square is equal to other square
        """
        return self.size == other.size

    def __ne__(self, other):
        """
        check if square is not equal to other square
        """
        return self.size != other.size

    def __gt__(self, other):
        """
        check if square is greater than other square
        """
        return self.size > other.size

    def __lt__(self, other):
        """
        check if square is less than other square
        """
        return self.size < other.size

    def __ge__(self, other):
        """
        check if square is greater than or equal to other square
        """
        return self.size >= other.size

    def __le__(self, other):
        """
        check if square is less than or equal to other square
        """
        return self.size <= other.size
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
