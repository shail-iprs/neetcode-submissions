class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        res=[1]*n
        for ind in range(1,n):
            if ratings[ind-1]<ratings[ind]:
                res[ind]=res[ind-1]+1
        
        for ind in range(n-2,-1,-1):
            if ratings[ind+1]<ratings[ind]:
                res[ind]=max(res[ind],res[ind+1]+1)
        return sum(res)