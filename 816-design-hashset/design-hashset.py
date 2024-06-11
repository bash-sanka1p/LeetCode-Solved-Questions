class MyHashSet:

    def __init__(self):
        self.hashset = set()
        # print(self.hashset)

    def add(self, key: int) -> None:
        if key not in self.hashset:
            self.hashset.add(key)
        # print(self.hashset)


    def remove(self, key: int) -> None:
        if key in self.hashset:
            self.hashset.remove(key)
        # print(self.hashset)



    def contains(self, key: int) -> bool:
        return True if  key in self.hashset else False
        # print(self.hashset)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)