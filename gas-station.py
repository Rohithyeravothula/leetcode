class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        loop_count = 0
        l = len(gas)
        ans = -1
        curpos = 0
        curgas = 0
        curtravel = 0
        while True:
            # print("O")
            # print(curpos, curgas, curtravel)
            loop_count += 1
            if loop_count > 2*l:
                break
            elif cost[curpos] > curgas + gas[curpos]:
                curpos = (curpos+1)%l
                curgas = 0
                curtravel = 0
            else:
                print(curpos, curgas, curtravel)
                curgas = curgas + gas[curpos] - cost[curpos]
                curpos = (curpos + 1)%l
                curtravel += 1
                if curtravel == l:
                    ans = curpos
                    break
        return ans



gas = [2,2,2]
cost = [2,8,2]
s = Solution()
s.canCompleteCircuit(gas, cost)


