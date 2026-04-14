class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m=len(heights)
        n=len(heights[0])

        visited=set()
        heap=[[0,0,0]]
        inds=[[0,1],[0,-1],[-1,0],[1,0]]
        while heap:
            diff,r,c=heapq.heappop(heap)

            if r==m-1 and c==n-1:
                return diff
            if (r,c) in visited:
                continue
            visited.add((r,c))
            for item in inds:
                nr,nc=r+item[0],c+item[1]
                if 0<=nr<m and 0<=nc<n:
                    heapq.heappush(heap,[max(diff,abs(heights[nr][nc]-heights[r][c])),nr,nc])
                    #visited.add((nr,nc))            