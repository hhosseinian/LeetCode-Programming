class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        n = len(asteroids)
        for i in range(n):
            while stack and asteroids[i]<0<stack[-1]:
                if stack[-1]<-asteroids[i]:
                    stack.pop()
                    continue
                    #stack.append(asteroids[i])
                elif stack[-1]==-asteroids[i]:
                    stack.pop()
                break
            else:
                stack.append(asteroids[i])
        return stack