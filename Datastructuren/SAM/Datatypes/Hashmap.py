class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


def createTableItem(key, val):
    T = Node(key, val)
    return T


class Hashmap:
    def __init__(self, type, n):
        """
        Type is een van "lin","quad","sep"
        n is de grootte van de hashmap
        """
        self.size = n
        self.map = n * [None]
        self.type = type

    def isEmpty(self):
        for i in self.map:
            if i is not None:
                return False
        return True

    def isFull(self):
        for i in self.map:
            if i is None:
                return False
        return True

    def tableInsert(self, param):
        index = param.key % self.size

        if self.type == "lin":
            if self.isFull():
                return False
            else:
                while self.map[index] is not None:
                    index = index + 1
                    if index > self.size - 1:
                        index = 0
                self.map[index] = param

        elif self.type == "quad":
            if self.isFull():
                return False
            else:
                var = 1
                cop = index
                while self.map[index] is not None:
                    index = cop + pow(var, 2)
                    var += 1
                    if index > self.size - 1:
                        index = index - self.size
                self.map[index] = param

        elif self.type == "sep":
            if self.map[index] is None:
                self.map[index] = param

            else:
                param.next = self.map[index]
                self.map[index].prev = param
                self.map[index] = param
        return True

    def tableRetrieve(self, key):
        if self.type == "lin" or self.type == "quad":
            for i in self.map:
                if i.key == key:
                    return i.val, True
            return False, False
        elif self.type == "sep":
            for i in self.map:
                if i is None:
                    continue
                else:
                    curr = i
                    while curr is not None:
                        if i.key == key:
                            return i.val,True
                        curr = curr.next

    def tableDelete(self, key):
        if self.type == "lin" or self.type == "quad":
            for i in range(0,self.size):
                if self.map[i] is None:
                    continue
                else:
                    if self.map[i].key == key:
                        self.map[i] = None
                        return True
            return False

        elif self.type == "sep":
            for i in range(0,self.size):
                if self.map[i] is None:
                    continue
                else:
                    node = self.map[i]
                    while node is not None:
                        if node.key == key:
                            if node.prev is None:
                                node.next.prev = None
                                return True
                            elif node.next is None:
                                node.prev.next = None
                                return True
                            else:
                                node.prev.next = node.next
                                node.next.prev = node.prev
                                return True
                        else:
                            node = node.next
            return False

    def save(self):
        if self.type == "lin" or self.type == "quad":
            dict = {}
            List = []
            for i in self.map:
                if i is None:
                    List.append(None)
                else:
                    List.append(i.val)
            dict['type'] = self.type
            dict['items'] = List
            return dict

        elif self.type == "sep":
            dict = {}
            List = []
            for i in self.map:
                if i is None:
                    List.append(None)
                else:
                    curr = i
                    temp = []
                    while curr is not None:
                        temp.append(curr.val)
                        curr = curr.next
                    List.append(temp)
            dict['type'] = self.type
            dict['items'] = List
            return dict

    def load(self, input):
        self.type = input['type']
        items = input['items']
        self.size = len(items)
        self.map = self.size * [None]
        if self.type == "lin" or self.type == "quad":
            for i in range(0,len(items)):
                if items[i] is None:
                    continue
                else:
                    self.map[i] = Node(items[i],items[i])
        elif self.type == "sep":
            for i in range(0,len(items)):
                if items[i] is None:
                    continue
                else:
                    temp = []
                    for j in range(0,len(items[i])):
                        temp.append(Node(items[i][j],items[i][j]))
                    for iter in range(0, len(temp)-1):
                        temp[iter].next = temp[iter+1]
                        temp[iter+1].prev = temp[iter]
                    self.map[i] = temp[0]


class HashmapTable(Hashmap):

    def __init__(self, type, n):
        super().__init__(type,n)

    def tableInsert(self, param):
        return super().tableInsert(param)

    def tableDelete(self, key):
        return super().tableDelete(key)
    def tableIsEmpty(self):
        return super().isEmpty()

    def save(self):
        return super().save()

    def load(self,input):
        super().load(input)


