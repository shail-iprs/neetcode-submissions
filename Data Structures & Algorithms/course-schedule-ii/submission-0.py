class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        indeg=[0]*numCourses

        for item in prerequisites:
            adj[item[1]].append(item[0])
            indeg[item[0]]+=1
        
        res=[]
        q=deque()
        for ind in range(len(indeg)):
            if indeg[ind]==0:
                res.append(ind)
                q.append(ind)

        while q:
            curr=q.popleft()
            for item in adj[curr]:
                indeg[item]-=1
                if indeg[item]==0:
                    res.append(item)
                    q.append(item)
        return res if len(res)==numCourses else []
            

        