# Implementatie van een arraybased queue
class MyQueue:
    def __init__(self, max):
        """
        Lege queue maken
        Pre-condition : maximum grote groter dan 0
        Post-condition : lege queue aangemaakt
        :param max: maximum grootte van de queue
        """
        self.items = [None] * max
        self.size = 0
        self.front = 0

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def getFront(self):
        if self.size == 0:
            return False, False
        return self.items[self.size - 1], True

    def enqueue(self, NieuwItem):
        if self.size == len(self.items):
            return False, False
        else:
            for i in range(self.size, -1, -1):
                j = i + 1
                self.items[j] = self.items[i]
            self.items[self.front] = NieuwItem
            self.size += 1
            return True

    def dequeue(self):
        if self.size == 0:
            return False, False
        else:
            x = self.items[self.size - 1]
            self.items[self.size - 1] = None
            self.size -= 1
            return x, True

    def save(self):
        l = self.items[self.front : self.size]
        return l

    def load(self, queue):
        self.items = queue
        self.size = len(queue)
