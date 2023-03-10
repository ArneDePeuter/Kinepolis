def createItem(key,val):
    return Item(key, val)

class Item:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
    
    def __lt__(self, other):
        return self.key < other.key

    def __eq__(self, other):
        return self.key == other.key

    def __str__(self) -> str:
        return "key: " + str(self.key) + ", val: " + str(self.val)

class Node():
    def __init__(self, item) -> None:
        self.item = item
        self.next = None

class MyStack():
    def __init__(self):
        self.top = None 
    
    def isEmpty(self):
        return (self.top==None)

    def getTop(self):
        if self.top!=None:
            return (self.top.value, self.top!=None)
        return (self.top, self.top!=None)

    def push(self,item): 
        node = Node(item) 
        if(self.top == None):
            self.top = node
        else:
            node.next = self.top 
            self.top = node
        return True

    def pop(self):
        if(self.top == None):
            return (None, False)
        else:
            node = self.top 
            self.top = node.next 
            node.next = None  
            item = node.item   
            del node
            return (item, self.top!=None)

    def save(self):
        l = []
        tgt = self.top
        while tgt!=None:
            l.insert(0, tgt.item)
            tgt = tgt.next
        return l

    def load(self, l):
        self.__init__()
        for elem in l:
            self.push(elem)
