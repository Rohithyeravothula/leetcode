class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        a = [0]*26
        for i in letters:
        	a[ord(i) - ord('a')] = 1
        # print(a)
        ans = None
        for i in range(1+ord(target) - ord('a'), 26):
        	if a[i] == 1:
        		ans = i
        		break
        if ans is None:
        	for i in range(0, 26):
        		if a[i] == 1:
        			ans = i
        			break
        # print(ans, ord(target)-ord('a'))
        return str(chr(ord('a') + ans))


a=["a", "e", "v"]
target = "x"
s=Solution()
print(s.nextGreatestLetter(a, target))
