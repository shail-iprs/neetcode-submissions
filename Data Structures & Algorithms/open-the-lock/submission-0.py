class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque

        # if target in deadends:
        #     return -1

        deadends=set(deadends)
        if "0000" in deadends:
            return -1

        q=deque()
        q.append("0000")
        deadends.add("0000")
        step=0
        while q:
            step+=1
            for _ in range(len(q)):
                curr=q.popleft()
                for ind in range(4):
                    for j in [1,-1]:
                        digit=str((int(curr[ind])+j+10)%10)
                        nlock=curr[:ind]+digit+curr[ind+1:]
                        
                        if nlock in deadends:
                            continue

                        if nlock==target:
                            return step

                        q.append(nlock)
                        deadends.add(nlock)

        return -1
            
            

