class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res=[]
        n=len(intervals)
        ind=0
        while ind <n and intervals[ind][1]<newInterval[0]:
            res.append(intervals[ind])
            ind+=1
        
        while ind <n and intervals[ind][0]<=newInterval[1]:
            newInterval[0]=min(intervals[ind][0],newInterval[0])
            newInterval[1]=max(intervals[ind][1],newInterval[1])
            print(newInterval)
            ind+=1
        res.append(newInterval)

        while ind <n:
            res.append(intervals[ind])
            ind+=1
        return res
