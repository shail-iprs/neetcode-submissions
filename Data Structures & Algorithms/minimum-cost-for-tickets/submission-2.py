class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n=len(days)
        dp={}
        def get(ind):
            if ind>=n:
                return 0
            if ind in dp:
                return dp[ind]
            i=ind
            while i<n and days[i]<days[ind]+1:
                i+=1
            one=costs[0]+get(i)

            i=ind
            while i<n and days[i]<days[ind]+7:
                i+=1
            two=costs[1]+get(i)

            i=ind
            while i<n and days[i]<days[ind]+30:
                i+=1
            
            three=costs[2]+get(i)

            res=min(one,two,three)
            dp[ind]=res
            return res
        return get(0)            