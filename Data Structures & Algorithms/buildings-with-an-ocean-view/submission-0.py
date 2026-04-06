class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        4,2,3,2,1
        4,3,2,2,1
        """

        """
        1,3,2,4,2,5,1
        1,1,2,2,3,4,5
        """

        stack=[]
        res=[]
        for ind in range(len(heights)):
            while stack and heights[stack[-1]]<=heights[ind]:
                k=stack.pop()
                #print(k)
            stack.append(ind)
        print(stack)
        return stack