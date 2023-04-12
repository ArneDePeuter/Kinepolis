def createItem(key, val):
    return Item(key, val)


class Item:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val

    def __lt__(self, other):
        if type(other) == type(self):
            return self.key < other.key
        else:
            return self.key < other

    def __eq__(self, other):
        if type(other) == type(self):
            return self.key == other.key
        else:
            return self.key == other

    def __repr__(self):
        return repr(self.val)

    def __getattr__(self, name):
        return getattr(self.val, name)


class Node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None


class MyStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def getTop(self):
        if self.top != None:
            return (self.top.value, self.top != None)
        return (self.top, self.top != None)

    def push(self, item):
        node = Node(item)
        if self.top == None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        return True

    def pop(self):
        if self.top == None:
            return (None, False)
        else:
            node = self.top
            self.top = node.next
            node.next = None
            item = node.item
            del node
            return (item, self.top != None)

    def save(self):
        l = []
        tgt = self.top
        while tgt != None:
            l.insert(0, tgt.item)
            tgt = tgt.next
        return l

    def load(self, l):
        self.__init__()
        for elem in l:
            self.push(elem)


class StackTable(MyStack):
    def __init__(self):
        super().__init__()

    # Checks if the table is empty
    def tableIsEmpty(self):
        """
        Checks if the table is empty

        Pre-conditions: None
        Post-conditions: Returns True if the table is empty
        """
        return self.isEmpty()

    # Inserts a TableItem to the table
    def tableInsert(self, item):
        """
        Inserts a TableItem to the table

        TableItem is of type twoThreeNode

        Pre-conditions: None
        Post-conditions: The treeItem gets inserted to the table
        """
        return self.push(item)

    # Retrieves an item from the table
    def tableRetrieve(self):
        """
        Retrieves an item from the table

        Pre-conditions: None
        Post-conditions: Returns a tuple (retrievedItem = item/None, done = True/False)
        """
        return self.getTop()

    # Deletes an item from the table
    def tableDelete(self, item):
        """
        Deletes an item from the table

        item is the target for deletion

        Pre-conditions: None
        Post-conditions: The given item gets deleted from the table
        """
        return self.pop()

    def createTableItem(self, key, val):
        return Item(key, val)
