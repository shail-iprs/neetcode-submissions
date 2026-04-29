class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for ind in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[ind]:
                temp=stack.pop()
                res[temp]=abs(temp-ind)
            stack.append(ind)
        return res