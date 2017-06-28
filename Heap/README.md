#HEAP

3 classes are exposed in this module, `Heap`, `MinHeap` & `MaxHeap` (todo).

## General use

###Create a heap:
```
heap = MinHeap()
```

###Create a heap with inital data:
```
heap = MinHeap([1, 2, 3])
```

###Create a heap with a value accessor.
Maybe you want to store a tuple in the form of `('whatever', [value])` -> `('a', 1)` in each node rather than an integer. Then we need to indicate to the `Heap` how to access the value it needs for ordering. We can do that by passing an accessor function as a second argument.
```
heap = MinHeap([1, 2, 3], lambda x: x[1]) # here we access the value
```
Defaults to identify function. i.e.: `lambda x: x`

##Heap
`Heap` follows the bellow invariant:
-
-

##MinHeap
`MinHeap` follows the bellow invariant: