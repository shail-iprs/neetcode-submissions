class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.q=deque()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.q.remove(key)
        self.q.appendleft(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key]=value
            self.q.remove(key)
            self.q.appendleft(key)
        else:
            if len(self.q)==self.capacity:
                temp=self.q.pop()
                del self.cache[temp]
            self.cache[key]=value
            self.q.appendleft(key)
