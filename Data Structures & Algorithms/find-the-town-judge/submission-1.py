class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indeg=[0]*(n+1)
        outdeg=[0]*(n+1)

        for item in trust:
            outdeg[item[0]]+=1
            indeg[item[1]]+=1


        for ind in range(n+1):
            if indeg[ind]==n-1 and outdeg[ind]==0:
                return ind
        return -1

