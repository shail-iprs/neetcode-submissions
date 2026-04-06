class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        mx_profit=0
        for ind in range(1,len(prices)):
            if prices[ind]<buy:
                buy=prices[ind]
            else:
                profit=prices[ind]-buy
                mx_profit=max(mx_profit,profit)
        return mx_profit