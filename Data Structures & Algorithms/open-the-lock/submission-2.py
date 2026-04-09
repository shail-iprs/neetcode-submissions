class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead=set(deadends)
        digits='0123456789'
        if target in dead:
            return -1
        start='0000'
        if target==start:
            return 0
        q=deque([(start,0)])
        visited=set([start])
        while q:
            curr,time=q.popleft()

            if curr==target:
                return time
            if curr in dead:
                continue
            for ind in range(4):
                change=int(curr[ind])
                for rev in [1,-1]:
                    d=(change+rev)%10
                    temp=curr[:ind]+str(d)+curr[ind+1:]
                    if temp not in dead and temp not in visited:
                        q.append((temp,time+1))
                        visited.add(temp)
                    
        return -1   


        