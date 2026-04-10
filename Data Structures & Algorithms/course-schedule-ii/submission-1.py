class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        indeg=[0]*(numCourses)
        res=[]
        for item in prerequisites:
            adj[item[1]].append(item[0])
            indeg[item[0]]+=1

        q=deque()
        for ind in range(numCourses):
            if indeg[ind]==0:
                q.append(ind)
                res.append(ind)
        
        while q:
            curr=q.popleft()

            for item in adj[curr]:
                if indeg[item]>0:
                    indeg[item]-=1
                    if indeg[item]==0:
                        q.append(item)
                        res.append(item)
        return res if len(res)==numCourses else []