from Datastructuren.SIEBE.Datatypes import MyBST

class BSTTable(MyBST):
    def __init__(self) -> None:
        super().__init__()

    #returns True if the ADT is empty
    def tableIsEmpty(self):
        return super().isEmpty()

    #Inserts an item into the ADT
    def tableInsert(self, item):
        return super().searchTreeInsert(item)

    #Deletes an item from the ADT
    def tableDelete(item, key):
        return super().searchTreeDelete(key)

    #Retrieves an item from the ADT
    def tableRetrieve(self, key):
        return super().searchTreeRetrieve(key)

    #InorderTraverses the table
    def traverseTable(self, func):
        super().inorderTraverse(func)

    # Saves the table as a dict
    def save(self):
        return super().save()

    # Loads the dict as a table
    def load(self, input):
        return super().load(input)

    #Creates an item that can be inserted into the ADT
    def createItem(self, key, val):
        return createTreeItem(key, val)
