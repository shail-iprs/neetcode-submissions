"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        start=[x.start for x in intervals]
        end=[x.end for x in intervals]

        start.sort()
        end.sort()

        print(start)
        print(end)
        s=0
        e=0
        count=0
        max_count=float('-inf')
        while s<len(start) and e<len(start):
            if start[s]<end[e]:
                count+=1
                s+=1
            else:
                count-=1
                e+=1
            max_count=max(max_count,count)
        return max_count