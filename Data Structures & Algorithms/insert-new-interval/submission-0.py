class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ind=0
        res=[]
        
        while ind < len(intervals) and intervals[ind][1]< newInterval[0]:
            res.append(intervals[ind])
            ind+=1

        
        while ind < len(intervals) and intervals[ind][0]<=newInterval[1]:
            newInterval[0]=min(intervals[ind][0],newInterval[0])
            newInterval[1]=max(intervals[ind][1],newInterval[1])
            ind+=1
        res.append(newInterval)

        while ind < len(intervals):
            res.append(intervals[ind])
            ind+=1
        return res