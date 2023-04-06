from Datastructuren.SAM.Datatypes import BST


def createTreeItem(key, val):
    return key, val


class BSTTable(BST):
    # Initialisatie BST
    def __init__(self):
        super().__init__()

    # Insert van een item
    def tableInsert(self, key,val):
        return super().searchTreeInsert(key,val)

    # Delete van een item
    def tableDelete(self, key):
        return super().searchTreeDelete(key)

    # Checkt of table leeg is
    def tableIsEmpty(self):
        return super().isEmpty()

    # Traverse van de tabel doen
    def traverseTable(self, func):
        super().inorderTraverse(func)

    # Retrieved object of waarde door op key te zoeken.
    def tableRetrieve(self, key):
        return super().searchTreeRetrieve(key)

    # Print de boom uit
    def save(self):
        return super().save()

    # Load een boom vanuit output van save
    def load(self, input):
        return super().load(input)

    def createItem(self, key, val):
        return createTreeItem(key, val)
