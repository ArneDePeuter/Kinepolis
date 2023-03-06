from Datastructuren.SAM.Datatypes import MyStack


class StackTable(MyStack):

    #Initialisatie Stack
    def __init__(self):
        super().__init__()

    #Insert van een item
    def tableInsert(self, item):
        return super().push(item)

    #Delete van een item
    def tableDelete(self, key):
        return super().pop(key)

    #Checkt of table leeg is
    def tableIsEmpty(self):
        return super().isEmpty()

    #Print de stack uit
    def save(self):
        return super().save()

    #Load een stack vanuit output van save
    def load(self, input):
        return super().load(input)