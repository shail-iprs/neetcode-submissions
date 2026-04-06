class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        sat=0
        not_sat=0
        mx=float('-inf')
        left=0
        for right in range(len(customers)):
            if grumpy[right]:
                not_sat+=customers[right]
            else:
                sat+=customers[right]
            
            while right-left+1>minutes:
                if grumpy[left]:
                    not_sat-=customers[left]
                    
                left+=1
            mx=max(mx,not_sat)
           
        return sat+mx
                