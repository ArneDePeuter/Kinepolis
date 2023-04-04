class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class LinkedChain:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def getLength(self):
        return self.length

    def retrieve(self, index):
        if self.getLength() < index:
            return False, False
        else:
            curr = self.head
            for i in range(0, index - 1):
                curr = curr.next
            return curr.value, True

    def insert(self, index, value):
        if index < 1 or index > self.length + 1:
            return False

        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            self.head.prev = self.tail
            self.head.next = self.tail
            self.tail.prev = self.head
            self.tail.next = self.head
        elif index == 1:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.head = new_node
            self.tail.next = self.head
        elif index == self.length + 1:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.head.prev = self.tail
        else:
            curr = self.head
            for i in range(1, index - 1):
                curr = curr.next
            new_node.next = curr.next
            curr.next.prev = new_node
            curr.next = new_node
            new_node.prev = curr
        self.length += 1
        return True

    def delete(self, index):
        if self.isEmpty() or index < 1 or index > self.length:
            return False

        if self.length == 1:
            self.head = None
            self.tail = None
        elif index == 1:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        elif index == self.length:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        else:
            curr = self.head
            for i in range(1, index):
                curr = curr.next
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        self.length -= 1
        return True

    def save(self):
        values = []
        curr = self.head
        for i in range(0, self.length):
            values.append(curr.value)
            curr = curr.next
        return values

    def load(self, input):
        self.head = None
        self.tail = None
        self.length = 0
        for i in range(0, len(input)):
            self.insert(i + 1, input[i])
