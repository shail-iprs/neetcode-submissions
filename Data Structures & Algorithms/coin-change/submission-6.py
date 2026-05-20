class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp={}
        def get(ind,target):
            if target==amount:
                return 0
            if ind>=n or target>amount:
                return float('inf')
            if (ind,target) in dp:
                return dp[(ind,target)]
            
            take=1+get(ind,target+coins[ind])
            not_take=get(ind+1,target)
            res=min(take,not_take)
            dp[(ind,target)]=res
            return res
        res=get(0,0)
        return res if res!=float('inf') else -1
