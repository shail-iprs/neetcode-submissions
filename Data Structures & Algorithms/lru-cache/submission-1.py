class Node:
    def __init__(self,key,val):
        self.key,self.val=key,val
        self.prev,self.next=None,None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.capacity=capacity

        self.head=Node(0,0)
        self.tail=Node(0,0)

        self.head.next=self.tail
        self.tail.prev=self.head
    
    def insert(self,node):
        prev,next,curr=self.tail.prev,self.tail.next,self.tail
        node.next=curr
        node.prev=prev
        node.prev.next=node
        curr.prev=node


    def remove(self,node):
        prev,next=node.prev,node.next
        prev.next,next.prev=next,prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.capacity:
            lru=self.head.next
            self.remove(lru)
            del self.cache[lru.key]    