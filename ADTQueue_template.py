"""
QUEUE REQUIREMENTS
vvvvvvvvvvvvvvvvvvvvvv
"""

class QueueWithWeirdFuncs:
    pass

class Queue(QueueWithWeirdFuncs):
    def __init__(self, maxHeap=True):
        super().__init__(maxHeap)

    def createItem(self, key, val):
        pass
    
    def isEmpty(self):
        pass

    def dequeue(self):
        pass
    
    def enqueue(self, item):
        pass
