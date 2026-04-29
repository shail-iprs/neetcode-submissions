class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        path=path.split('/')
        for item in path:
            if item in ['.','']:
                pass
            elif item=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        return '/'+"/".join(stack)