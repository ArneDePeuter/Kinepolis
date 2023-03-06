class Heap:
    def __init__(self, isMaxHeap=True):
        self.root = None
        self.isMaxheap = isMaxHeap
        pass

    def heapIsEmpty(self):
        return self.root is None

    def heapDelete(self):
        if self.root is None:
            return [None, False]
        else:
            value = self.root.value
            # heeft root 2 kinderen?
            if self.root.left is not None and self.root.right is not None:
                # kies een tak en haal het
                if self.isMaxheap:
                    node = self.root.maxRootNode()
                else:
                    node = self.root.minRootNode()
                node.removeFromParent()
                swap(node, self.root)
                self.root.trickleDown(self.isMaxheap)
            #  enkel linker child?
            elif self.root.left is not None:
                self.root = self.root.left
            #  enkel rechter child?
            elif self.root.right is not None:
                self.root = self.root.right
            # geen children
            else:
                self.root = None
            return [value, True]

    def heapInsert(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            node = self.root.insert(item, self.isMaxheap)
            node.trickleUp(self.isMaxheap)
        return True

    def heapRetrieve(self, key):
        pass

    def save(self):
        if self.root is None:
            return "{}"
        else:
            return self.root.save()

    def load(self, dict):
        self.root = loadNode(dict, None)


def swap(a, b):
    temp = a.value
    a.value = b.value
    b.value = temp


def safeValue(node):
    if node is None:
        return "None"
    else:
        return node.save()


def loadNode(dict, parent):
    if dict is None:
        return None
    else:
        value = dict.get('root')
        node = Node(value, parent)
        children = dict.get('children')
        if children is not None:
            node.left = loadNode(children[0], node)
            node.right = loadNode(children[1], node)
        return node


class Node:
    def __init__(self, value=None, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def insert(self, value, isMaxHeap):
        if self.left is None:
            self.left = Node(value, self)
            return self.left

        if self.right is None:
            self.right = Node(value, self)
            return self.right

        if isMaxHeap:
            if self.left.value < self.right.value:
                return self.right.insert(value, isMaxHeap)
            else:
                return self.left.insert(value, isMaxHeap)
        else:
            if self.left.value > self.right.value:
                return self.right.insert(value, isMaxHeap)
            else:
                return self.left.insert(value, isMaxHeap)

    def trickleUp(self, isMaxHeap):
        if self.parent is not None:
            if isMaxHeap and self.value > self.parent.value:
                swap(self, self.parent)
                self.parent.trickleUp(isMaxHeap)
            elif not isMaxHeap and self.value < self.parent.value:
                swap(self, self.parent)
                self.parent.trickleUp(isMaxHeap)

    def trickleDown(self, isMaxHeap):
        # heeft node 2 kinderen?
        if self.left is not None and self.right is not None:
            if isMaxHeap:
                if self.left.value < self.right.value:
                    self.trickleDownConditionally(self.right, isMaxHeap)
                else:
                    self.trickleDownConditionally(self.left, isMaxHeap)
            else:
                if self.left.value < self.right.value:
                    self.trickleDownConditionally(self.right, isMaxHeap)
                else:
                    self.trickleDownConditionally(self.right, isMaxHeap)
        #  enkel rechter child?
        if self.right is not None:
            self.trickleDownConditionally(self.right, isMaxHeap)
        #  enkel linker child?
        if self.left is not None:
            self.trickleDownConditionally(self.left, isMaxHeap)
        # geen children
        else:
            pass

    def trickleDownConditionally(self, node, isMaxHeap):
        if isMaxHeap and self.value < node.value:
            swap(self, node)
            node.trickleDown(isMaxHeap)
        elif not isMaxHeap and self.value > node.value:
            swap(self, node)
            node.trickleDown(isMaxHeap)

    def save(self):
        # workaround voor niet consistent spatie gebruik in string waarmee in test vergeleken wordt, zou normaal niet
        # nodig moeten zijn in echte code
        if self.parent is None:
            space = " "
        else:
            space = ""

        if self.left is None and self.right is None:
            return "{'root':" + space + str(self.value) + "}"
        else:
            return "{'root':" + space + str(self.value) + ",'children':[" + safeValue(self.left) + "," + safeValue(
                self.right) + "]}"

    def minRootNode(self):
        if self.left is None and self.right is None:
            return self
        elif self.left is None:
            return self.right.minRootNode()
        elif self.right is None:
            return self.left.minRootNode()
        elif self.left.value < self.right.value:
            return self.left.minRootNode()
        else:
            return self.right.minRootNode()

    def maxRootNode(self):
        if self.left is None and self.right is None:
            return self
        elif self.left is None:
            return self.right.maxRootNode()
        elif self.right is None:
            return self.left.maxRootNode()
        elif self.left.value < self.right.value:
            return self.right.maxRootNode()
        else:
            return self.left.maxRootNode()

    def hasAtLeastOneChild(self):
        return self.left is not None or self.right is not None

    def removeFromParent(self):
        if self.parent is not None:
            if self.parent.left == self:
                self.parent.left = None
            elif self.parent.right == self:
                self.parent.right = None
            self.parent = None
