"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x : x.start)
        #print(intervals)
        first=intervals[0]

        ind=1
        while ind < len(intervals):
            if first.start<=intervals[ind].start<first.end:
                return False
            first=intervals[ind]
            ind+=1
        return True