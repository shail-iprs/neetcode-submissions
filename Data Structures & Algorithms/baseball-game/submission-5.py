class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]

        for item in operations:
            if item=='+':
                if stack and len(stack)>=2:
                    stack.append(stack[-1]+stack[-2])
            elif item=='D':
                if stack and len(stack)>=1:
                    stack.append(stack[-1]*2)
            elif item=='C':
                if stack and len(stack)>=1:
                    stack.pop()
            else:
                stack.append(int(item))
        return sum(stack)