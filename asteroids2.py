class Solution:
    def asteroidCollision(self, asteroids: 'List[int]') -> 'List[int]':
        stk = []
        i = 0
        l = len(asteroids)
        while i<l:
            if asteroids[i] < 0:
                while stk and stk[-1] > 0 and stk[-1] < -asteroids[i]:
                    stk.pop()
                print(stk)
                if not stk or stk[-1] <= 0:
                    stk.append(asteroids[i])
                elif stk and stk[-1] == -asteroids[i]:
                    stk.pop()
            else:
                stk.append(asteroids[i])
            i+=1
        return stk

inp = [8, -8]
inp = [-8, 8]
print(Solution().asteroidCollision(inp))
