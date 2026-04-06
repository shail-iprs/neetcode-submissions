class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks)%4!=0:
            return False
        
        length=sum(matchsticks)//4

        sides=[0]*4
        matchsticks.sort(reverse=True)
        
        def dfs(k):
            seen=set()
            if k==len(matchsticks):
                return True

            for ind in range(4):
                if sides[ind] in seen:
                    continue
                if sides[ind]+matchsticks[k]<=length:
                    seen.add(sides[ind])
                    sides[ind]+=matchsticks[k]
                    
                    if dfs(k+1):
                        return True
                    sides[ind]-=matchsticks[k]
                
            return False
        return dfs(0)