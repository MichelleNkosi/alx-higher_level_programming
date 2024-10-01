#!/usr/bin/python3
"""Defines classes for a singly linked list and its node."""

class Node:
    """Represents a node in a singly linked list."""
    
    def __init__(self, data, next_node=None):
        """Initializes a new Node.
        
        Args:
            data (int): The data stored in the node.
            next_node (Node): The next node in the list (default is None).
        
        Raises:
            TypeError: If data is not an integer or next_node is not a Node or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for the data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for the data attribute.
        
        Args:
            value (int): The data to be stored in the node.
        
        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for the next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for the next_node attribute.
        
        Args:
            value (Node or None): The next node in the list.
        
        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""
    
    def __init__(self):
        """Initializes an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """Defines the string representation of the list.
        
        Returns:
            str: A string showing all the node data, one per line.
        """
        node = self.__head
        values = []
        while node is not None:
            values.append(str(node.data))
            node = node.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position (increasing order).
        
        Args:
            value (int): The value to insert.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node is not None and 
                   current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
