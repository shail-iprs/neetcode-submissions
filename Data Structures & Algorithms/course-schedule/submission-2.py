class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=defaultdict(list)
        indeg=[0]*(numCourses)

        for item in prerequisites:
            adj[item[1]].append(item[0])
            indeg[item[0]]+=1

        q=deque()
        count=0
        for ind in range(numCourses):
            if indeg[ind]==0:
                q.append(ind)
                count+=1
        
        while q:
            curr=q.popleft()

            for item in adj[curr]:
                if indeg[item]>0:
                    indeg[item]-=1
                    if indeg[item]==0:
                        count+=1
                        q.append(item)
        return count==numCourses

