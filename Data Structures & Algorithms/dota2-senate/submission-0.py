class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rq=deque()
        dq=deque()
        n=len(senate)
        for ind in range(len(senate)):
            if senate[ind]=='R':
                rq.append(ind)
            else:
                dq.append(ind)
        
        while rq and dq:
            r=rq.popleft()
            d=dq.popleft()

            if r<d:
                rq.append(r+n)
            else:
                dq.append(d+n)
        return "Radiant" if rq else "Dire"
