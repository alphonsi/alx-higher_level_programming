#!/usr/bin/python3
<<<<<<< HEAD
class Node:
    def __init__(self, data, next_node=None):
=======
""" """


class Node:
    """
    defines node
    """

    def __init__(self, data, next_node=None):
        """
        initializes node

        Attributes:
            data: data stored in node
            next_node: address of next node in list
        """
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
<<<<<<< HEAD
=======
        """
        finds data
        """
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
        return self.__data

    @data.setter
    def data(self, value):
<<<<<<< HEAD
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
=======
        """
        validates that data is an integer
        """
        if type(value) is not int:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        finds next_node
        """
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
<<<<<<< HEAD
        if value is not None and type(value) != Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        ret = ""
        node = self.head
        while node:
            ret += str(node.data) + "\n"
            node = node.next_node
        return ret[:-1]

    def sorted_insert(self, value):
        new = Node(value)
        if not self.head:
            self.head = new
            return

        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return

        node = self.head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        if node.next_node:
            new.next_node = node.next_node
        node.next_node = new
=======
        """
        validates next_node as either None or a node
        """
        if type(value) is not Node and value is not None:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    defines singly linked list class
    """

    def __init__(self):
        """
        initializes singly linked list
        """
        self.__head = None

    def __str__(self):
        """
        returns string version of list
        """
        string = ""
        if self.__head is None:
            return string
        runner = self.__head
        while runner is not None:
            string += str(runner.data)
            runner = runner.next_node
            if runner is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """
        inserts a new node into correct position in list
        """
        if self.__head is None or value < self.__head.data:
            self.__head = Node(value, self.__head)
            return
        runner = self.__head
        while runner.next_node is not None and runner.next_node.data < value:
            runner = runner.next_node
        runner.next_node = Node(value, runner.next_node)
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
