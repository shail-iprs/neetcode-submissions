class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1=len(s1)
        l2=len(s2)
        l3=len(s3)
        dp={}
        def dfs(i,j,k):
            if (i,j,k) in dp:
                return dp[(i,j,k)]
            
            if k==l3:
                return i==l1 and j==l2
            
            res=False
            if i<l1 and s1[i]==s3[k]:
                res=dfs(i+1,j,k+1)
            
            if not res and j<l2 and s2[j]==s3[k]:
                res=dfs(i,j+1,k+1)
            dp[(i,j,k)]=res
            return res
        
        return dfs(0,0,0)