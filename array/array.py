#!/usr/bin/env python

"""
Custom implementation of array data structure
"""


class Array:
    def __init__(self, capacity: int):
        """
        capacity : number of items to be stored in the array
        """
        if not isinstance(capacity, int):
            raise TypeError("capacity should be an int")
        self.capacity = capacity
        self.container = [None] * capacity

    def __str__(self):
        """
        prints the array items
        """
        return " ".join(str(item) for item in self.container)

    def capacity(self):
        """
        returns number of items array can hold
        """
        return self.capacity

    def __len__(self):
        """
        returns the current length of elements not total capacity
        """
        count = 0
        for i in self.container:
            if i is not None:
                count = count + 1
        return count

    def size(self):
        """
        returns the number of items in array
        """
        return self.__len__()

    def is_empty(self):
        """
        returns true if array has no value else false
        """
        for item in self.container:
            if item is not None:
                return False
        return True

    def __getitem__(self, index):
        """
        retrieves an elemnt at a specifc index
        index: where a element is located in array
        usage: my_array[index]
        returns  an element a specific index in an array
        """
        if index >= self.capacity:
            raise IndexError(
                f"index does not exist. Valid index {self.capacity - self.capacity} - {self.capacity - 1}"
            )
        return self.container[index]

    def at(self, index):
        """
        returns an item at a given index.
        blows up if index out of bounce
        """
        return self.__getitem__(index)

    def __setitem__(self, index: int, value: any):
        """
        update an element at a specific index
        index: location in array to add the value
        value: value to be set
        usage: my_array[index] = value
        """
        if index >= self.capacity:
            raise IndexError(
                f"index does not exist. Valid index {self.capacity - self.capacity} - {self.capacity - 1}"
            )
        self.container[index] = value

    def remove_by_index(self, index=None):
        """
        remove an item from array
        index: index of item to be removed
        """
        if index is None:
            raise ValueError("Provide an index of item to be removed")

        item_to_remove = None
        if index is not None:
            if not isinstance(index, int):
                raise ValueError("Index should be an int")
            index = int(index)
            if index >= self.capacity:
                raise IndexError(
                    f"index does not exist. Valid index {self.capacity - self.capacity} - {self.capacity - 1}"
                )
            item_to_remove = self.container[index]
            self.container[index] = None
        return item_to_remove

    def remove_by_value(self, value=None):
        """
        remove an item from array
        value: the item to be remved
        """
        if value is None:
            raise ValueError("Provide a value to be removed")

        item_to_remove = None
        if value is not None:
            for index, item in enumerate(self.container):
                if item == value:
                    item_to_remove = self.container[index]
                    self.container[index] = None
        if not item_to_remove:
            return None
        return item_to_remove
