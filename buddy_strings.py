from collections import Counter
class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
        	return False

        if A == B:
        	counterA = Counter(A)
        	if len(A) == len(counterA):
        		return False
        	return True

        l = len(A)
        count = 0
        mapping = {}
        for i in range(0, l):
        	if A[i] != B[i]:
        		count += 1
        		if count > 2:
        			return False
        		mapping[A[i]] = B[i]

        if len(mapping) != 2:
        	return False
        k = list(mapping.keys())
        if mapping[k[0]] == k[1] and mapping[k[1]] == k[0]:
        	return True
        return False

s = Solution()
print(s.buddyStrings("aaaaaaacb", "aaaaaaabc"))
