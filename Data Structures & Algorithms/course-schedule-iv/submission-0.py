class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj=defaultdict(set)

        indeg=[0]*numCourses

        pre=defaultdict(set)
        for item in prerequisites:
            adj[item[0]].add(item[1])
            indeg[item[1]]+=1
        
        q=deque()
        for ind in range(len(indeg)):
            if indeg[ind]==0:
                q.append(ind)
        
        while q:
            curr=q.popleft()
            for neighbour in adj[curr]:
                pre[neighbour].add(curr)
                pre[neighbour].update(pre[curr])
                indeg[neighbour]-=1
                if indeg[neighbour]==0:
                    q.append(neighbour)
        
        return [item[0] in pre[item[1]] for item in queries]