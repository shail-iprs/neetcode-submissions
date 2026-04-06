class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        adj=defaultdict(list)
        indeg=[0]*n
        for item in pre:
            adj[item[1]].append(item[0])
            indeg[item[0]]+=1
        
        from collections import deque
        q=deque()

        for ind in range(n):
            if indeg[ind]==0:
                q.append(ind)
        step=0
        while q:
            curr=q.popleft()
            step+=1
            for item in adj[curr]:
                if indeg[item]>0:
                    indeg[item]-=1
                    if indeg[item]==0:
                        q.append(item)
        return n==step


