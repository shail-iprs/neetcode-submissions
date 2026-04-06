class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=defaultdict(list)
        indeg=[0]*numCourses

        for item in prerequisites:
            adj[item[1]].append(item[0])
            indeg[item[0]]+=1
        
        cnt=0
        q=deque()

        for ind in range(len(indeg)):
            if indeg[ind]==0:
                q.append(ind)
                cnt+=1
        
        while q:
            curr=q.popleft()
            for item in adj[curr]:
                indeg[item]-=1
                if indeg[item]==0:
                    q.append(item)
                    cnt+=1

        return cnt==numCourses

