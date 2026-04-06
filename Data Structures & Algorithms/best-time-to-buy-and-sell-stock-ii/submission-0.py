class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        buy=prices[0]
        for ind in range(1,len(prices)):
            if buy>prices[ind]:
                buy=prices[ind]
            else:
                profit+=prices[ind]-buy
                buy=prices[ind]
        return profit