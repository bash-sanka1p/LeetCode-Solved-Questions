class MyHashSet:

    def __init__(self):
        self.hashset = {}
        # print(self.hashset)

    def add(self, key: int) -> None:
        if key not in self.hashset.keys():
            self.hashset[key]=1
        # print(self.hashset)


    def remove(self, key: int) -> None:
        if key in self.hashset.keys():
            del self.hashset[key]
        # print(self.hashset)



    def contains(self, key: int) -> bool:
        return True if  key in self.hashset.keys() else False
        # print(self.hashset)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)