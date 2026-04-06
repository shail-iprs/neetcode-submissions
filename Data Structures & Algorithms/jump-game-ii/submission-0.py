class Solution:
    def jump(self, nums: List[int]) -> int:
        q=deque()
        q.append((0,0))
        min_step=float('inf')
        visited=set([0])
        while q:
            ind,step=q.popleft()
            if ind==len(nums)-1:
                return step
            
            for idx in range(1,nums[ind]+1):
                if ind+idx<=len(nums)-1 and ind+idx not in visited:
                    visited.add(ind+idx)
                    q.append((ind+idx,step+1))
    