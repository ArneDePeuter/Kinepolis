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
            self.hashmap[hash].append(object)
        else:
            self.hashmap[hash] = [object]
        return (hash, self.hashmap[hash].index(object))

if __name__ == "__main__":
    from Film import Film
    newmovie = Film(0, "123", 0)
    newmovie1 = Film(0, "321", 0)
    gen = SearchKeyGenerator()
    print(gen.getSearchKey(newmovie))
    print(gen.getSearchKey(newmovie1))
    print(gen.hashmap)