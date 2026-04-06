class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        start=0
        n=len(s)
        q=deque(([start]))

        visited=set([start])

        while q:
            ind=q.popleft()
            print(ind)
            if ind==n-1:
                return True

            for idx in range(ind+minJump,min(ind+maxJump,n-1)+1):
                if 0<=idx<=n-1 and s[idx]=='0' and idx not in visited:
                    visited.add(idx)
                    q.append(idx)
        return False



