class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for item in tokens:
            if item.lstrip('-').isdigit():
                stack.append(float(item))
            elif item=='*':
                if len(stack)>=2:
                    a,b=stack.pop(),stack.pop()
                    stack.append(a*b)
            elif item=='+':
                if len(stack)>=2:
                    a,b=stack.pop(),stack.pop()
                    stack.append(a+b)
            elif item=='-':
                if len(stack)>=2:
                    a,b=stack.pop(),stack.pop()
                    stack.append(b-a)
            elif item=='/':
                if len(stack)>=2:
                    a,b=stack.pop(),stack.pop()
                    stack.append(int(b/a))
        print(stack)
        return int(stack[0])
                