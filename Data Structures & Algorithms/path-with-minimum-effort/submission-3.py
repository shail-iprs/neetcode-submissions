class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m=len(heights)
        n=len(heights[0])
        inds=[[0,1],[0,-1],[-1,0],[1,0]]

        heap=[[0,0,0]]
        visit=set()
        
        #max_diff=float('-inf')
        
        while heap:
            diff,r,c=heapq.heappop(heap)
            if (r,c) in visit:
                continue
            visit.add((r,c))
            if r==m-1 and c==n-1:
                return diff
            
            for item in inds:
                nr,nc=r+item[0],c+item[1]
                if 0<=nr<m and 0<=nc<n and (nr,nc) not in visit:
                    max_diff=max(diff,abs(heights[r][c]-heights[nr][nc]))
                    heapq.heappush(heap,(max_diff,nr,nc))
            

