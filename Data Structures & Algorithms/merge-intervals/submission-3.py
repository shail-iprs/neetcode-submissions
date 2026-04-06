class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res=[intervals[0]]
        n=len(intervals)
        for ind in range(1,n):
            #curr=intervals[ind]
            if res[-1][0]<=intervals[ind][0]<=res[-1][1]:
                res[-1][0]=min(res[-1][0],intervals[ind][0])
                res[-1][1]=max(res[-1][1],intervals[ind][1])
            else:
                res.append(intervals[ind])
            prev=intervals[ind]
        return res