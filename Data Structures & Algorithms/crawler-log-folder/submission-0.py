class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]

        for item in logs:
            if item=='../':
                if stack:
                    stack.pop()
            elif item!='./':
                stack.append(item)
        print(stack)
        return len(stack)