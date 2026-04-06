class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        res=0
        max_res=0
        ind=1
        while ind < len(prices):
            res=prices[ind]-buy
            if res>0:
                max_res=max(res,max_res)
            else:
                buy=prices[ind]
            ind+=1
        return max_res