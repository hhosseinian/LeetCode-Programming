class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = OrderedDict()
    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        else:
            self.values[key] = self.values.pop(key)
            return self.values[key]

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.values.move_to_end(key)
        self.values[key]=value
        if len(self.values) > self.capacity:
            self.values.popitem(last = False)
                
            



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)