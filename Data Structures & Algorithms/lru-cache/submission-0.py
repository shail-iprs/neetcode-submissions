from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        
        self.cache={}
        self.queue=deque()
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.queue.remove(key)
            self.queue.appendleft(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.queue.remove(key)
        else:
            if len(self.cache)==self.capacity:
                least=self.queue.pop()
                del self.cache[least]
       
        self.cache[key]=value
        self.queue.appendleft(key)
        print(self.cache)
