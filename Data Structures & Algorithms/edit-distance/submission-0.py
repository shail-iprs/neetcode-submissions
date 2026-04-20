class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        dp={}
        def getdist(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i==m:
                return n-j
            if j==n:
                return m-i
            res=0
            if word1[i]==word2[j]:
                res=getdist(i+1,j+1)
            else:
                insert=getdist(i,j+1)
                delete=getdist(i+1,j)
                update=getdist(i+1,j+1)
                res=1+min(insert,delete,update)
            dp[(i,j)]=res
            return dp[(i,j)]
        return getdist(0,0)