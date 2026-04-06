class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        count=1
        while self.stack and self.stack[-1][1]<=price:
            temp=self.stack.pop()
            count+=temp[0]
        self.stack.append([count,price])
        return count



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)