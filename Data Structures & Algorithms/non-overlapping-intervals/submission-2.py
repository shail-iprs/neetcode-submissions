class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x :x[0])
        print(intervals)
        
        prev_end=intervals[0][1]
        n=len(intervals)
        res=0
        for ind in range(1,n):
            start,end=intervals[ind]
            if prev_end>start:
                res+=1
                prev_end=min(end,prev_end)
            else:
                prev_end=end
        return res
