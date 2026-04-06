class Solution:
    def maxSatisfied(self, customer: List[int], grumpy: List[int], minutes: int) -> int:
        left=0
        win=0
        sat=0
        mx=float('-inf')
        for right in range(len(customer)):
            if grumpy[right]:
                win+=customer[right]
            else:
                sat+=customer[right]
            if right-left+1>minutes:
                if grumpy[left]:
                    win-=customer[left]
                left+=1
            
            mx=max(win,mx)
        return mx+sat