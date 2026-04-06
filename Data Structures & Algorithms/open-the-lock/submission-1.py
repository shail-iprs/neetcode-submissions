class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends=set(deadends)
        if '0000' in deadends:
            return -1
        
        if target=='0000':
            return 0
        
        q=deque()
        q.append('0000')
        deadends.add('0000')
        steps=0
        while q:
            steps+=1
            for _ in range(len(q)):
                curr=q.popleft()
                for ind in range(4):
                    for j in [1,-1]:
                        d=int(curr[ind])
                        if j==1:
                            d= d+1 if d<9 else 0
                        elif j==-1:
                            d=d-1 if d>0 else 9
                        d=str(d)

                        temp=curr[:ind]+d+curr[ind+1:]

                        if temp==target:
                            return steps
                        
                        if temp in deadends:
                            continue
                        
                        q.append(temp)
                        deadends.add(temp)
        return -1

