from ..Datatypes.Heap import Heap, createItem


class PriorityQueue:
    def __init__(self):
        self.heap = Heap(maxHeap=False)

    def isEmpty(self):
        return self.heap.heapIsEmpty()

    def dequeue(self):
        item, succes = self.heap.heapDelete()
        if succes:
            return [item.val, succes]
        else:
            return [None, succes]

    def enqueue(self, key, val):
        return self.heap.heapInsert(createItem(key, val))