class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : (x[1]))
        print(intervals)
        
        first=intervals[0]

        ind =1
        res=0
        while ind < len(intervals):
            if first[1]>intervals[ind][0]:
                res+=1
            else:
                first=intervals[ind]
            ind+=1
        return res