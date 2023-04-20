from kinepolis.Datastructuren.CEDRIC.DataTypes.heap import Heap, Node

class PrioQueue:
    def __init__(self, maxQueue=True, heap=Heap):
        self.datastruct = heap(maxQueue)

    def isEmpty(self) -> bool:
        return self.datastruct.heapIsEmpty()

    def dequeue(self) -> Node:
        return self.datastruct.heapDelete()

    def enqueue(self, key, val) -> bool:
        return self.datastruct.heapInsert(Node(key, val))
