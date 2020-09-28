class RingBuffer:
    """
    RingBuffer Class

    Parameters:

    capacity : int
    size : int
    write_index : int
    storage : list

    Methods:
     - append
         adds the given element to the buffer

     - get
          returns all the elements in the buffer in a list
          in their given order
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.write_index = 0
        self.storage = []

    def append(self, item):
        if self.size >= self.capacity:
            self.storage[self.write_index] = item
        else:
            self.storage.append(item)
            self.size += 1

        if self.write_index < (self.capacity - 1):
            self.write_index += 1
        else:
            self.write_index = 0

    def get(self):
        return self.storage