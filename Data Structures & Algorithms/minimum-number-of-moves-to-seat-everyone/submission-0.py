class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res=0
        for ind in range(len(seats)):
            res+=abs(students[ind]-seats[ind])
        return res