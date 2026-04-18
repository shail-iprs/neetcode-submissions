class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp={}
        n=len(stones)
        def minweight(ind,diff):
            if (ind,diff) in dp:
                return dp[(ind,diff)]
            if ind==n:
                return diff
            dp[(ind,diff)]=min(minweight(ind+1,diff+stones[ind]),
            minweight(ind+1,abs(diff-stones[ind])))
            return dp[(ind,diff)]
        return minweight(0,0)