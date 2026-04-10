class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj=defaultdict(list)
        indeg=[0]*numCourses

        for item in prerequisites:
            adj[item[0]].append(item[1])
            indeg[item[1]]+=1
        
        q=deque()
        for ind in range(numCourses):
            if indeg[ind]==0:
                q.append(ind)
        
        pre=defaultdict(set)

        while q:
            curr=q.popleft()
            for item in adj[curr]:
                pre[item].add(curr)
                pre[item].update(pre[curr])
                indeg[item]-=1
                if indeg[item]==0:
                    q.append(item)
        
        return [u in pre[v] for u,v in queries]


