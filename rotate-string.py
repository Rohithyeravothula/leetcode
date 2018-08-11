class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
        	return False
        N = A+A
        if B in N:
        	return True
        return False

s=Solution()
print(s.rotateString("abcd", ""))



