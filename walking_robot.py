from collections import defaultdict
class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        turns = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def get_dir(cur, turn):
            if turn == -1:
                turn = 1
            elif turn == -2:
                turn = -1

            return turns[(turns.index(cur) + turn + 4)%4]



        x_obs = defaultdict(list)
        y_obs = defaultdict(list)
        for x, y in obstacles:
            x_obs[x].append(y)
            y_obs[y].append(x)

        for x in x_obs:
            x_obs[x].sort()

        for y in y_obs:
            y_obs[y].sort()


        # def get_obs(cur):
        #     if cur[0]:
        #         return y_obs
        #     return x_obs

        def get_lh(a, b):
            if a < b:
                return a, b
            return b, a


        x=0
        y=0
        direction = (0, 1)
        for cmd in commands:
            if cmd == -1 or cmd == -2:
                direction = get_dir(direction, cmd)
            else:
                x1 = x+(direction[0]*cmd)
                y1 = y+(direction[1]*cmd)
                print(direction, x, y, x1, y1)
                if x1!=x:
                    xl, xh = get_lh(x, x1)
                    po=x1
                    for po in y_obs[y]:
                        if po >= xl and po <= xh:
                            x1 = po - direction[0]*1
                            break

                if y1!=y:
                    yl, yh = get_lh(y, y1)
                    po=y1
                    for po in x_obs[x]:
                        if po >= yl and po <= yh:
                            y1=po - direction[1]*1
                            break
                x=x1
                y=y1

        return x**2 + y**2


commands = [7,-2,-2,7,5]
obstacles=[[-3,2],[-2,1],[0,1],[-2,4],[-1,0],[-2,-3],[0,-3],[4,4],[-3,3],[2,2]]
 # = [[0, 3]]
s = Solution()
print(s.robotSim(commands, obstacles))







""
