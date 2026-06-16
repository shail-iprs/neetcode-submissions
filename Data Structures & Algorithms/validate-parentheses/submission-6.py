class Solution:
    def isValid(self, s: str) -> bool:

        def check(first,last):
            return first+last in ['{}','()','[]']
        stack=[]

        for item in s:
            if item in ['(','{','[']:
                stack.append(item)
            elif stack and check(stack[-1],item):
                    stack.pop()
            else:
                return False
        return len(stack)==0