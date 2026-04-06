class StockSpanner:

    def __init__(self):
        self.plist=[]

    def next(self, price: int) -> int:
        c=1
        while self.plist and price>=self.plist[-1][0]:
            temp=self.plist.pop()
            c+=temp[1]
        self.plist.append((price,c))
        return c


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)