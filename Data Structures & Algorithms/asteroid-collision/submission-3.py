class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for item in asteroids:
            alive=True
            while stack and item<0<stack[-1]:
                if stack[-1]<-item:
                    stack.pop()
                elif abs(stack[-1])==abs(item):
                    stack.pop()
                    alive=False
                    break
                else:
                    alive=False
                    break
            if alive:
                stack.append(item)
        return stack