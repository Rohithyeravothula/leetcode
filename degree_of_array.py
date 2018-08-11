from collections import Counter
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        max_freq = counter[max(counter, key=lambda x: counter[x])]
        interested = set()
        for key in counter:
        	if counter[key] == max_freq:
        		interested.add(key)

        l = len(nums)
        ends = {}
        for i in range(0, l):
        	if nums[i] in ends:
        		ends[nums[i]] = i
        	else:
        		ends[nums[i]] = i

        min_sub = l
        for i in range(0, l):
        	if nums[i] in interested:
        		min_sub = min(min_sub, ends[nums[i]] - i + 1)
        		interested.remove(nums[i])
        return min_sub

inpnums = [1,2,3,4]
s=Solution()
print(s.findShortestSubArray(inpnums))
        