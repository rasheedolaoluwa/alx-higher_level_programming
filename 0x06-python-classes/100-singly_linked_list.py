#!/usr/bin/python3

"""Define classes for a singly-linked list."""


class Node:
    """
    Represent a node in a singly-linked list.

    Attributes:
        __data (int): The data held by the Node.
        __next_node (Node): The next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node, optional): The next node in the linked list.
            Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data of the Node.

        Returns:
            int: The data stored in the Node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data of the Node.

        Args:
            value (int): The new data for the Node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Get the next node in the linked list.

        Returns:
            Node: The next Node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the linked list.

        Args:
            value (Node): The new next node for the current Node.

        Raises:
            TypeError: If value is not a Node object and is not None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represent a singly-linked list.

    Attributes:
        __head (Node): The head node of the linked list.
    """

    def __init__(self):
        """
        Initialize a new SinglyLinkedList.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the SinglyLinkedList in sorted order.

        Args:
            value (int): The data for the new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """
        Define the string representation of a SinglyLinkedList.

        Returns:
            str: A string representation of the linked list data.
        """
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(values)
