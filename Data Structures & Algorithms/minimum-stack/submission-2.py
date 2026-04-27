class MinStack:

    def __init__(self):
        self.min_stack=[]
        self.full=[]

    def push(self, val: int) -> None:
        self.full.append(val)
        if not self.min_stack or val<=self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        res=self.full.pop()
        if self.min_stack and res==self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.full[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
