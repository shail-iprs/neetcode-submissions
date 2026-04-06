class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack=[]
        for item in ops:
            print(stack)
            if item=='+':
                if len(stack)>=2:
                    a,b=stack[-1],stack[-2]
                    stack.append(a+b)
            elif item=='D':
                if stack:
                    stack.append(stack[-1]*2)
            elif item=='C':
                if stack:
                    stack.pop()
            else:
                stack.append(int(item))
        return sum(stack)