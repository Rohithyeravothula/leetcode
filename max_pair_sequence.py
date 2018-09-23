class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if not pairs:
            return 0
        pairs.sort(key=lambda x: x[1])
        l = len(pairs)
        counts = [1]*l
        i = 1
        while i<l:
            j = 0
            ci, cj = pairs[i]
            while j<i:
                pi, pj = pairs[j]
                if pj < ci:
                    counts[i] = max(counts[i], counts[j]+1)
                j+=1
            i+=1
        # print(max(counts))
        return max(counts)



        
i1 = [[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]]
i1 = [[0,0], [1,2], [3,4]]
Solution().findLongestChain(i1)