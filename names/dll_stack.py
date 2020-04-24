import sys
sys.path.append('../ring_buffer')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0

        """
        Why is our DLL a good choice to store our elements?
        
        A Stack pushs and pops elements with the "Last in, first out" rule. That means it just adds and removes
        items at the tail. A linked list is good for this because it can handle these actions pretty fast. The
        operations could be done with an array as well.
        """
        
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_tail()

    def len(self):
        if self.size > 0:
            return self.size
        else:
            return 0