from .ADTfactory import ADTFactory

class NonUniqueWrap:
    def __init__(self, table) -> None:
        self.table = table() 
    def tableInsert(self, key, val):
        if self.table.tableIsEmpty():
            newList = ADTFactory.getADT("NonUniqueList")
            newList.insert(newList.size+1, val)
            self.table.tableInsert(key, newList)
            return
        
        item, succes = self.table.tableRetrieve(key)
        if succes:
            item.insert(item.size+1, val)
        else:
            newList = ADTFactory.getADT("NonUniqueList")
            newList.insert(newList.size+1, val)
            self.table.tableInsert(key, newList)
    
    def traverseTable(self, func):
        l = []
        self.table.traverseTable(l.append)
        items = []
        for LLitem in l:
            items.extend(list(LLitem.save()))
        for item in items:
            func(item)

    def tableRetrieve(self, key):
        item, succes = self.table.tableRetrieve(key)
        if not succes:
            return None, False
        else:
            return list(item.save())[0], True
