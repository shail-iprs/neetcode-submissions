class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp={}
        def get(ind):
            if ind==n:
                return 1
            if s[ind]=='0':
                return 0
            if ind in dp:
                return dp[ind]
            ans=0
            
            ans+=get(ind+1)
            if ind+1<n and 10<=int(s[ind:ind+2])<=26:
                ans+=get(ind+2)
            dp[ind]=ans
            return ans
        return get(0)