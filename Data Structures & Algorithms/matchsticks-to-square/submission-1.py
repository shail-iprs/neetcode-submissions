class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks)%4!=0:
            return False
        
        length=sum(matchsticks)//4

        sides=[0]*4
        matchsticks.sort(reverse=True)
        seen=set()
        def dfs(k):

            if k==len(matchsticks):
                return True

            for ind in range(4):
                if sides[ind]+matchsticks[k]<=length:
                    sides[ind]+=matchsticks[k]
                    if dfs(k+1):
                        return True
                    sides[ind]-=matchsticks[k]
                if sides[ind]==0:
                    break
            return False
        return dfs(0)