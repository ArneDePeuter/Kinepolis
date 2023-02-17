def createTableItem(key, val):
    return val

class Node:
    """
    A doublelinked chain node
    """
    def __init__(self, value=None) -> None:
        """
        Initialises a Node

        @param: value is the value the node stores

        preconditions: None
        postcondition: Creates a Node object
        """
        self.value = value
        self.next = None
        self.previous = None
    
    def retrieve(self, value):
        """
        Retrieves a node with a given value

        preconditions: None
        postcondition: Returns the node and a bool if it was retrieved or not
        """
        #value found
        if self.value==value:
            return [self, True]
        else:
            #can look further
            if self.next!=None:
                return self.next.retrieve(value)
            #at the end, value not found
            else:
                return [None, False]

class DoubleLinkedChain:
    """
    A double linked chain object
    """
    def __init__(self) -> None:
        """
        Initialises a linked chain object with a empty Headnode

        preconditions: None
        postconditions: double linked chain object gets created
        """
        self.head = Node() #Node with default value = None
    
    def isEmpty(self):
        """
        Checks if the chain is empty

        preconditions: None
        postconditions: returns a bool (True if empty/False otherwise)
        """
        return self.head.value == None

    def toList(self):
        """
        Returns a python list with the values of the linked chain

        preconditions: None
        postconditions: Returns None if the chain is empty
                        Returns a list with the values if the chain is not empty
        """
        l = []
        target = self.head
        if self.isEmpty(): 
            return None #empty chain so return None
        l.append(target.value) #append head val
        while target.next is not None: #while we can go further
            target = target.next #go further
            l.append(target.value) #add values
        return l
    
    def insert(self, value):
        """
        Inserts a value to the front of the chain

        preconditions: None
        postconditions: Inserts the value to the front of the chain, always return True
        """
        if self.isEmpty():
            self.head.value = value #if the chain is empty we can insert directly
            return True #we inserted
        newRoot = Node(value) #create a new Node 
        self.head.previous = newRoot #set prev from head to this node
        newRoot.next = self.head #set next from this node to head
        self.head = newRoot #move head
        return True #we inserted
    
    def retrieve(self, value):
        """
        Retrieves a node with a given value

        preconditions: None
        postcondition: Returns the node and a bool if it was retrieved or not
        """
        return self.head.retrieve(value)
    
    def delete(self, value):
        """
        Deletes a value from the chain

        preconditions: None
        postconditions: returns a bool (if value deleted -> True/ else False)
        """
        #value is in head
        if value==self.head.value:
            self.head = self.head.next #move the head or head becomes None
            if self.head is None:
                self.head = Node() #if head was None create empty head
            return True #we deleted
        else:
            
            if self.head.next is None:
                return False #val not found
            node, succes = self.head.next.retrieve(value) #retrieve node we delete
            if not succes:
                return False #val not found
            node.previous.next = node.next 
            if node.next is not None:
                node.next.previous = node.previous
            return True

class Hashmap:
    """
    Hashmap object
    """
    def __init__(self, type, n) -> None:
        """
        Initialises the Hashmap

        type is een van "lin","quad","sep"
        n is de grootte van de hashmap

        preconditions: None
        postconditions: hashmap object gets created
        """
        self.type = type
        self.size = n
        self.hashTable = [None]*n
    
    def isEmpty(self):
        """
        Checks if the hashmap is empty

        preconditions: None
        postconditions: returns a bool (if the hashmap is empty -> True/ else False)
        """
        return self.hashTable==[None]*self.size

    def createLinIndex(self, item):
        """
        Creates the index for a hashmap using linear probing

        preconditions: None
        postconditions: returns an int if there is space, else return None
        """
        h = item%self.size
        startH = h
        while self.hashTable[h]!=None:
            h+=1
            if h>self.size-1:
                h=0
            if h==startH:
                return None
        return h
    
    def createQuadIndex(self, item):
        """
        Creates the index for a hashmap using quadratic probing

        preconditions: None
        postconditions: returns an int if there is space, else return None
        """
        h = item%self.size
        startH = h
        i = 1
        while True:
            if self.hashTable[h] is None:
                return h
            h = (startH + i**2)%self.size
            i += 1
            if h>self.size-1:
                startH=0
                i=1
            if h==startH:
                return None
        
    def getLinIndex(self, item):
        """
        Returns the index for a hashmap using linear probing

        preconditions: None
        postconditions: returns an int if the item is found, else return None
        """
        h = item%self.size
        startH = h
        while self.hashTable[h]!=item:
            h+=1
            if h>self.size-1:
                h=0
            if h==startH:
                return None
        return h
    
    def getQuadIndex(self, item):
        """
        Returns the index for a hashmap using quadratic probing

        preconditions: None
        postconditions: returns an int if the item is found, else return None
        """
        h = item%self.size
        startH = h
        i = 1
        while True:
            if self.hashTable[h] == item:
                return h
            h = (startH + i**2)%self.size
            i += 1
            if h>self.size-1:
                startH=0
                i=1
            if h==startH:
                return None

    def tableInsert(self, item):
        """
        Inserts an item to the hashing table

        preconditions: None
        postconditions: returns a bool if the item is inserted
        """
        if self.type == 'sep':
            h = item%self.size
            if self.hashTable[h] is None:
                newItem = DoubleLinkedChain()
                newItem.insert(item)
                self.hashTable[h] = newItem
            else:
                self.hashTable[h].insert(item)
            return True
    
        if self.type=='lin':
            h = self.createLinIndex(item)
        elif self.type=='quad':
            h = self.createQuadIndex(item)
        if h is None:
            return False
        self.hashTable[h] = item
        return True
    
    def tableRetrieve(self, item):
        """
        Retrieves an item from the hashmap

        preconditions: None
        postconditions: returns the value and a bool (found -> True else False)
        """
        if self.isEmpty():
            return [None, False]
        if self.type == 'sep':
            h = item%self.size
            if self.hashTable[h] is not None:
                node, succes = self.hashTable[h].retrieve(item)
                return [node.value, succes]
            else:
                return [None, False]
        if self.type=='lin':
            h = self.getLinIndex(item)
        elif self.type == 'quad':
            h = self.getQuadIndex(item)
        if h is None:
            return [None, False]
        return [self.hashTable[h], True]

    def tableDelete(self, item):
        """
        Deletes an item from the hashmap

        preconditions: None
        postconditions: returns a bool (deleted item -> True else False)
        """
        if self.isEmpty():
            return [None, False]
        if self.type == 'sep':
            h = item%self.size
            if self.hashTable[h] is not None:
                return self.hashTable[h].delete(item)
            else:
                return False
        if self.type=='lin':
            h = self.getLinIndex(item)
        elif self.type == 'quad':
            h = self.getQuadIndex(item)
        if h is None:
            return False
        self.hashTable[h] = None
        return True

    def save(self):
        """
        Saves the current hashtable in a dictionary

        preconditions: None
        postconditions: returns a dictionary with all the values from the hashmap
        """
        if self.type=='sep':
            l = []
            for item in self.hashTable:
                if item is None:
                    l.append(item)
                else:
                    l.append(item.toList())
            return {'type': self.type, 'items' : l}
        return {'type': self.type, 'items' : self.hashTable}
    
    def load(self, d):
        """
        Loads a hashmap in from a given dictionary

        preconditions: None
        postconditions: A new hashmap is created from the given dictionary
        """
        self.__init__(d['type'], len(d['items']))
        self.hashTable = d['items']
        if self.type == 'sep':
            for i, itemL in enumerate(self.hashTable):
                if itemL is not None:
                    chain = DoubleLinkedChain()
                    for item in reversed(itemL): #reversed because we insert
                        chain.insert(item)
                    self.hashTable[i] = chain

class HashmapTable(Hashmap):
    def __init__(self, type, n) -> None:
        super().__init__(type, n)
    
    def tableIsEmpty(self):
        return self.isEmpty()