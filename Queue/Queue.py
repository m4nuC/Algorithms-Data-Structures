from functools import reduce

class Queue:
    def __init__(self, initial_data):
        self.items = []
        if initial_data and isinstance(initial_data, list):
            self.items = initial_data
        elif initial_data:
            self.items.append(initial_data)

    def enqueue(self, item):
        self.items.append(item)
        return self.items

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return '>>'.join([str(x) for x in self.items])