class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        l = len(asteroids)
        if l == 0:
            return asteroids
        i = 1
        stack = [asteroids[0]]
        while i<l:
            if len(stack) == 0:
                stack.append(asteroids[i])
                i+=1
            else:
                cur = stack[-1]
                if cur < 0:
                    stack.append(asteroids[i])
                    i+=1
                elif asteroids[i] < 0:
                    if abs(asteroids[i]) == cur:
                        stack.pop()
                        i+=1
                    elif abs(asteroids[i]) > cur:
                        stack.pop()
                    else:
                        i+=1
                else:
                    stack.append(asteroids[i])
                    i+=1
        return stack

a = [10,2, -4, 10]
s=Solution()
ans = s.asteroidCollision(a)
print(ans)