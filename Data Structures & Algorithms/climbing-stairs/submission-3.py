class Solution:
    def climbStairs(self, n: int) -> int:
        prev1,prev2=1,1

        for ind in range(2,n+1):
            curr=prev1+prev2
            prev1=prev2
            prev2=curr
        return prev2