def hashItemList(l):
    total = 0
    for item in l:
        for c in str(item):
            total += ord(c)
    return total

class SearchKeyGenerator:
    def __init__(self) -> None:
        self.hashmap = {}
    
    def getSearchKey(self, object):
        hash = object.hash()
        if (hash in self.hashmap):
            l = self.hashmap[hash]
            for item in l:
                if item==object:
                    return (hash, self.hashmap[hash].index(item)), False
            self.hashmap[hash].append(object)
        else:
            self.hashmap[hash] = [object]
        return (hash, self.hashmap[hash].index(object)), True

if __name__ == "__main__":
    from Film import Film
    gen = SearchKeyGenerator()
    key, newItem = gen.getSearchKey(Film(0, "321", 0))
    print(f"key: {key}, newItem: {newItem}")
    key, newItem = gen.getSearchKey(Film(0, "123", 0))
    print(f"key: {key}, newItem: {newItem}")
    key, newItem = gen.getSearchKey(Film(0, "123", 0))
    print(f"key: {key}, newItem: {newItem}")