import sys
sys.path.append('../ring_buffer')
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        
        """
        Why is our DLL a good choice to store our elements?
        
        A Queue is there to add elements to the tail and remove elements from the head. On linked lists 
        adding and removing elements from head and tail as a complexity of O(1)
        """
        
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        if self.size > 0:
            return self.size
        else:
            return 0