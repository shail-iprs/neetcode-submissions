class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length=sum(matchsticks)
        if total_length%4!=0:
            return False
        
        length=total_length//4
        matchsticks.sort(reverse=True)
        sides=[0]*4
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
        