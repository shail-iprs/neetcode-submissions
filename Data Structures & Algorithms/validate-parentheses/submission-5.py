class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        def check(item,stack):
            temp=stack[-1]+item
            return temp in ['{}','[]','()']
        for item in s:
            if item in ['(','[','{']:
                stack.append(item)
            else:
                if stack and check(item,stack):
                    stack.pop()
                else:
                    return False
        return len(stack)==0