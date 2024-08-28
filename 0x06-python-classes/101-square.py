#!/usr/bin/python3
<<<<<<< HEAD
"""Square module."""


class Square:
    """Defines a square."""

    def __str__(self):
        """Returns string representation."""
        return self.my_sprint()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """Constructor.

        Args:
            size: Length of a side of the square.
            position: Position of the square.
=======


class Square:
    """
    creates square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        initializes square

        Args:
            size: size of side of square
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
        """
        self.size = size
        self.position = position

    @property
    def size(self):
<<<<<<< HEAD
        """Property for the length of a side of this square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
=======
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

    @property
    def position(self):
        """Property for the position of this square.

        Raises:
            TypeError: If value is not tuple of 2 positive integers.
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
        """
        return self.__size ** 2

    @property
    def position(self):
        """
        finds position
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
        """
        return self.__position

    @position.setter
    def position(self, value):
<<<<<<< HEAD
        if not isinstance(value, tuple) or len(value) != 2 or \
         len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Area of this square.

        Returns:
            The size squared.
        """
        return self.__size ** 2

    def my_sprint(self):
        """Returns string representation of this square."""
        ret = ""
        if not self.size:
            return "\n"

        for i in range(self.position[1]):
                ret += "\n"
        for i in range(self.size):
            for j in range(self.position[0]):
                ret += " "
            for j in range(self.size):
                ret += "#"
            ret += "\n"
        return ret

    def my_print(self):
        """Prints this square."""
        print(self.my_sprint(), end="")
=======
        """
        sets position

        Args:
            value: position of the square
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """
        prints square with character #
        """
        if self.__size == 0:
            print("")
            return
        for i in range(self.position[1]):
            print("")
        for i in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))

    def __str__(self):
        """
        returns string version of square
        """
        string = ""
        if self.__size == 0:
            return string
        string += '\n' * self.__position[1]
        for i in range(self.__size):
            string += " " * self.__position[0]
            string += "#" * self.__size
            if i < self.__size - 1:
                string += "\n"
        return string
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
