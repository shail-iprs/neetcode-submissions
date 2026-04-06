class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x :x[0])
        res=[intervals[0]]
        ind=1

        while ind < len(intervals):
            first=res[-1]
            second=intervals[ind]
            if first[1]<second[0]:
                res.append(second)
            else:
                first[1]=max(first[1],second[1])
            ind+=1
        return res