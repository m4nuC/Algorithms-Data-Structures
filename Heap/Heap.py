import sys
import math

class Heap:
    def __init__(self, A = []):
        self.heap = A

    def children_indexes(self, i):
        return (i*2+1, i*2+2)

    def get_children(self, i):
        left_i, right_i = self.children_indexes(i)
        if self.size()-1 >= right_i:
            return [(left_i, self.heap[left_i]), (right_i, self.heap[right_i])]
        elif self.size()-1 >= left_i:
            return [(left_i, self.heap[left_i]), (right_i, math.inf)]
        else:
            return [(left_i, math.inf), (right_i, math.inf)]

    def get_min_children(self, i):
        left_i, right_i = self.children_indexes(i)
        if self.size()-1 >= right_i:
            return (left_i, self.heap[left_i]) if self.heap[left_i] < self.heap[right_i] else (right_i, self.heap[right_i])
        elif self.size()-1 >= left_i:
            return (left_i, self.heap[left_i])
        else:
            return False

    def parent(self, i):
        return math.ceil(i/2) -1

    def add(self, x):
        self.heap.append(x)

    def size(self):
        return len(self.heap)

    def swap(self, i, j):
        print('swapping', i, j)
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp

    def last(self):
        print('last item', self.heap[len(self.heap)-1])

    def __str__(self):
        heapified_tree = ', '.join(map(str, self.heap))
        if self.size() == 0: return heapified_tree
        levels = math.ceil(math.log(self.size()))
        for lvl in range(0, levels+1):
            for cell in range(2**lvl-1, 2**(lvl+1)-1):
                if cell < len(self.heap):
                    sys.stdout.write( ' {} '.format(self.heap[cell]) )
            sys.stdout.write('\n')
        return heapified_tree


class MinHeap(Heap):
    def __init__(self, A = []):
        self.heap = []
        [self.add(a) for a in A]

    def add(self, x):
        super().add(x)
        self.min_heapify_up(self.parent(self.size()-1))

    def min_heapify_up(self, i):
        candidate = self.get_min_children(i)
        if candidate and self.heap[i] > candidate[1]:
            self.swap(i, candidate[0])
            parent = self.parent(i)
            if parent >= 0:
                return self.min_heapify_up(parent)


h = MinHeap([12, 4, 3, 1, 5, 7, 8, 2])
print(h)

