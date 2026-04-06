class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks)%4!=0:
            return False
        matchsticks.sort(reverse=True)
        n=len(matchsticks)
        req=sum(matchsticks)//4
        sides=[0,0,0,0]
        def dfs(start):
            if start==n:
                return True
            
            for end in range(4):
                if sides[end]+matchsticks[start]<=req:
                    sides[end]+=matchsticks[start]
                    if dfs(start+1):
                        return True
                    sides[end]-=matchsticks[start]
            return False
            

        return dfs(0)
        

