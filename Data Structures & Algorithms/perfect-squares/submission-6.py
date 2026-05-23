class Solution:
    def numSquares(self, n: int) -> int:
        import sys
        sys.setrecursionlimit(10**6)
        dp={}
        def get(curr):
            if curr==0:
                return 0

            if curr in dp:
                return dp[curr]
            res=float('inf')
            n1=int(math.sqrt(curr))
            for item in range(1,n1+1):
                if curr-item*item<0:
                    break
                res=min(res,1+get(curr-item*item))
            dp[curr]=res
            return res
        return get(n)