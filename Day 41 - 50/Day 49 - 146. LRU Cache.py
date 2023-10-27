class DLLNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key, Node
        self.left, self.right = DLLNode(0, 0), DLLNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def removeNode(self, node: DLLNode):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        del node

    def insertNode(self, node: DLLNode):
        prev, nxt = self.right.prev, self.right
        node.prev = prev
        prev.next = nxt.prev = node
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.removeNode(self.cache[key])
            self.insertNode(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])
        self.cache[key] = DLLNode(key, value)
        self.insertNode(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.removeNode(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)