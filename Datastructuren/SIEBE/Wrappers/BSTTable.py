from Datastructuren.SIEBE.Datatypes import MyBST, createTreeItem

class BSTTable(MyBST):
    def __init__(self) -> None:
        self.bst = MyBST()

    #returns True if the ADT is empty
    def tableIsEmpty(self):
        return self.bst.isEmpty()

    #Inserts an item into the ADT
    def tableInsert(self, item):
        return self.bst.searchTreeInsert(item)

    #Deletes an item from the ADT
    def tableDelete(self, key):
        return self.bst.searchTreeDelete(key)

    #Retrieves an item from the ADT
    def tableRetrieve(self, key):
        return self.bst.searchTreeRetrieve(key)

    #InorderTraverses the table
    def traverseTable(self, func):
        return self.bst.inorderTraverse(func)

    # Saves the table as a dict
    def save(self):
        return self.bst.save()

    # Loads the dict as a table
    def load(self, input):
        return self.bst.load(input)

    #Creates an item that can be inserted into the ADT
    def createItem(self, key, val):
        return createTreeItem(key, val)
