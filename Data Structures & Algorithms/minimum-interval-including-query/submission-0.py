import heapq

class Solution:
    def minInterval(self, intervals, queries):
        
        def get_res(val):
            heap = [[item[1] - item[0] + 1, item[0], item[1]] for item in intervals]
            heapq.heapify(heap)  # ✅ make it a heap
            
            check = float('inf')
            
            while heap:
                length, start, end = heapq.heappop(heap)
                
                # ✅ correct interval check
                if start <= val <= end:
                    check = length
                    break   
            
            return check if check != float('inf') else -1  
        
        res = []
        for item in queries:
            res.append(get_res(item))  
        
        return res