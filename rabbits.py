from collections import Counter
class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        counter = Counter(answers)
        rabbits = 0
        for key in counter:
        	rabbits += (1+key)*(counter[key]//(key+1))
        	if counter[key]%(1+key):
        		rabbits += (1+key)
        return rabbits
s=Solution()
print(s.numRabbits([1,0,0]))