class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj=defaultdict(list)

        for i in range(len(points)):
            x1,y1=points[i]
            for j in range(i+1,len(points)):
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        
        visited=set()

        heap=[[0,0]]
        total=0
        while len(visited)<len(points):
            dist,cord=heapq.heappop(heap)

            if cord in visited:
                continue
            
            visited.add(cord)
            
            total+=dist

            for item in adj[cord]:
                if item[1] not in visited:
                    heapq.heappush(heap,[item[0],item[1]])

        return total
