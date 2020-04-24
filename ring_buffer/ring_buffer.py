from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            self.current.value = item
            if self.current == self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        node = self.storage.head

        while node:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0 
        self.storage = [None] * self.capacity

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            self.current += 1
        else: 
            self.current += 1
            self.storage[(self.current % self.capacity) -1] = item

    def get(self):
        content = []

        for e in self.storage:
            if e != None:
                content.append(e)
        
        return content
        


buffer = RingBuffer(3)

print(buffer.get())   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

print(buffer.get())   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

print(buffer.get())   # should return ['d', 'e', 'f']

# --------------------------------------------------------------------

buffer2 = ArrayRingBuffer(3)

print(buffer2.get())   # should return []

buffer2.append('a')
buffer2.append('b')
buffer2.append('c')

print(buffer2.get())   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer2.append('d')

print(buffer2.get())   # should return ['d', 'b', 'c']

buffer2.append('e')
buffer2.append('f')

print(buffer2.get())   # should return ['d', 'e', 'f']