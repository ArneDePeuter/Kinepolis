from Datastructuren.CEDRIC.DataTypes.heap import Heap, Node


class PriorityQueue(Heap):
    def __init__(self, maxHeap=True):
        super().__init__(maxHeap)

    def createItem(self, key, val):
        return Node(key, val)

    def isEmpty(self):
        return self.heapIsEmpty()

    def dequeue(self):
        return self.heapDelete()

    def enqueue(self, item):
        return self.heapInsert(item)
