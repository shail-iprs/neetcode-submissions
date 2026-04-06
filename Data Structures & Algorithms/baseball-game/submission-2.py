class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]

        for item in operations:
            #print(stack)
            if item.lstrip('-').isdigit():
                stack.append(int(item))
            elif item=='+':
                if len(stack)>=2:
                    b=stack[-1]
                    a=stack[-2]
                    stack.append(a+b)
            elif item=='C':
                if stack:
                    stack.pop()
            elif item=='D':
                if stack:
                    stack.append(stack[-1]*2)
        return sum(stack)