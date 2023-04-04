class Node:
    def __init__(self, value_, next_, previous_):
        """

        :param value_:
        :param next_:
        :param previous_:
        """
        self.value = value_
        self.next = next_
        self.previous = previous_


class LinkedChain:
    def __init__(self):
        self.listHead = Node(None, None, None)
        self.listHead.next = self.listHead
        self.listHead.previous = self.listHead

    def isEmpty(self):
        if self.listHead.next is self.listHead:
            return True
        else:
            return False

    def getLength(self):
        if self.listHead.next is None:
            return 0
        else:
            length = 0
            pointer = self.listHead
            while pointer.next.value is not None:
                length += 1
                pointer = pointer.next
            return length

    def retrieve(self, position):
        if position > self.getLength() or position <= 0 or self.listHead is None:
            return tuple((None, False))

        else:
            if position <= self.getLength() / 2:
                pointer = self.listHead
                for _ in range(position):
                    pointer = pointer.next
                return tuple((pointer.value, True))
            else:
                pointer = self.listHead
                for _ in range(position):
                    pointer = pointer.previous
                return tuple((pointer.value, True))

    def insert(self, position, value):
        if position - 1 > self.getLength() or position <= 0:
            return False

        else:
            if position <= self.getLength() / 2:
                pointer = self.listHead
                for _ in range(position - 1):
                    pointer = pointer.next
            else:
                pointer = self.listHead
                for _ in range(self.getLength() - position + 2):
                    pointer = pointer.previous

            tempNext = pointer.next
            newNode = Node(value, tempNext, pointer)
            pointer.next = newNode
            newNode.next.previous = newNode

            return True

    def save(self):
        result = "["
        pointer = self.listHead.next
        result += str(pointer.value)

        for _ in range(1, self.getLength()):
            pointer = pointer.next
            result += "," + str(pointer.value)

        return result + "]"

    def load(self, itemList):
        for _ in range(self.getLength()):
            self.delete(1)

        for position in range(len(itemList)):
            self.insert(position + 1, itemList[position])

    def delete(self, position):
        if position - 1 > self.getLength() or position <= 0:
            return False

        else:
            if position <= self.getLength() / 2:
                pointer = self.listHead
                for _ in range(position - 1):
                    pointer = pointer.next
            else:
                pointer = self.listHead
                for _ in range(self.getLength() - position + 2):
                    pointer = pointer.previous

            pointer.next = pointer.next.next
            pointer.next.previous = pointer
            return True


if __name__ == "__main__":
    l = LinkedChain()
    print(l.isEmpty())
    print(l.getLength())
    print(l.retrieve(4)[1])
    print(l.insert(4, 500))
    print(l.isEmpty())
    print(l.insert(1, 500))
    print(l.retrieve(1)[0])
    print(l.retrieve(1)[1])
    print(l.save())
    print(l.insert(1, 600))
    print(l.save())
    l.load([10, -9, 15])
    l.insert(3, 20)
    print(l.delete(0))
    print(l.save())
    print(l.delete(1))
    print(l.save())


# True
# 0
# False
# False
# True
# True
# 500
# True
# [500]
# True
# [600,500]
# False
# [10,-9,20,15]
# True
# [-9,20,15]
