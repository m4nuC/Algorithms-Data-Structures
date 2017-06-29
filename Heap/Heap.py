import sys
import math

class Heap:
    def __init__(self, A = [], value_accessor = lambda x: x):
        self.heap = A
        self.value_accessor = value_accessor

    def children_indexes(self, i):
        return (i*2+1, i*2+2)

    def get_children(self, i):
        left_i, right_i = self.children_indexes(i)
        if self.size()-1 >= right_i:
            return [(left_i, self.value_accessor(self.heap[left_i])), (right_i, self.value_accessor(self.heap[right_i]))]
        elif self.size()-1 >= left_i:
            return [(left_i, self.value_accessor(self.heap[left_i])), (right_i, math.inf)]
        else:
            return [(left_i, math.inf), (right_i, math.inf)]

    def get_min_child(self, i):
        left_i, right_i = self.children_indexes(i)
        if self.size()-1 >= right_i:
            return (left_i, self.value_accessor(self.heap[left_i])) if self.value_accessor(self.heap[left_i] )< self.value_accessor(self.heap[right_i]) else (right_i, self.value_accessor(self.heap[right_i]))
        elif self.size()-1 >= left_i:
            return (left_i, self.value_accessor(self.heap[left_i]))
        else:
            return (False, False)

    def get_max_child(self, i):
        left_i, right_i = self.children_indexes(i)
        if self.size()-1 >= right_i:
            return (left_i, self.value_accessor(self.heap[left_i])) if self.value_accessor(self.heap[left_i] )> self.value_accessor(self.heap[right_i]) else (right_i, self.value_accessor(self.heap[right_i]))
        elif self.size()-1 >= left_i:
            return (left_i, self.value_accessor(self.heap[left_i]))
        else:
            return (False, False)

    def parent(self, i):
        index = math.ceil(i/2) -1
        return index if index > -1 else False

    def add(self, x):
        self.heap.append(x)

    def size(self):
        return len(self.heap)

    def swap(self, i, j):
        print('swapping {} and {}'.format( self.heap[i], self.heap[j]))
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp

    def last(self):
        return self.heap[len(self.heap)-1]

    def __str__(self):
        heapified_tree = ', '.join(map(str, self.heap))
        if self.size() == 0: return heapified_tree
        levels = math.ceil(math.log(self.size()))
        for lvl in range(0, levels+1):
            for cell in range(2**lvl-1, 2**(lvl+1)-1):
                if cell < len(self.heap):
                    sys.stdout.write( ' {} '.format(self.heap[cell]) )
            sys.stdout.write('\n')
        return ''

class MinHeap(Heap):
    def __init__(self, A = [], value_accessor = lambda x: x):
        self.value_accessor = value_accessor
        self.heap = []
        [self.add(a) for a in A]

    def add(self, x):
        super().add(x)
        self.min_heapify_up(self.size()-1)

    def pluck_min(self):
        self.swap(0, self.size()-1)
        min = self.heap.pop()
        self.min_heapify_down(0)
        return min

    def pluck(self, i):
        index, value = self.get_min_child(i)
        if i == self.size()-1:
            return self.heap.pop(i)
        elif index:
            self.swap(i, index)
            return self.pluck(index)
        else:
            self.swap(i, i+1)
            return self.pluck(i+1)

    def min_heapify_up(self, i):
        parent = self.parent(i)
        if parent is False: return
        if self.value_accessor(self.heap[i]) < self.value_accessor(self.heap[parent]):
            self.swap(i, parent)
            return self.min_heapify_up(parent)

    def min_heapify_down(self, i):
        index, value = self.get_min_child(i)
        if index and self.value_accessor(self.heap[i]) > value:
            self.swap(i, index)
            return self.min_heapify_down(index)
