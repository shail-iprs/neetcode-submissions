class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res=[0]*len(temp)
        stack=[]
        for ind in range(len(temp)):
            
            while stack and temp[ind]>stack[-1][1]:
                i,v=stack.pop()
                res[i]=ind-i
            #print(ind,count)
            stack.append([ind,temp[ind]])
        return res