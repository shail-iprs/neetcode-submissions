class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indeg=[0]*(n+1)
        outdeg=[0]*(n+1)

        for item in trust:
            indeg[item[1]]+=1
            outdeg[item[0]]+=1
        
        for ind in range(1,n+1):
            if outdeg[ind]==0 and indeg[ind]==n-1:
                return ind
        return -1