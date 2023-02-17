class Node():
    def __init__(self, value) -> None:
        self.value = value
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

    def push(self,value): 
        node = Node(value) 
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
            value = node.value   
            del node
            return (value, self.top!=None)

    def save(self):
        l = []
        tgt = self.top
        while tgt!=None:
            l.insert(0, tgt.value)
            tgt = tgt.next
        return l

    def load(self, l):
        self.__init__()
        for elem in l:
            self.push(elem)