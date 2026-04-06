class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap=[]
        trips.sort(key=lambda x : x[1])
        
        curr=0
        for p,s,e in trips:
            while heap and heap[0][1]<=s:
                curr-=heapq.heappop(heap)[0]
            curr+=p
            if curr>capacity:
                return False
            heapq.heappush(heap,(p,e))
        return True