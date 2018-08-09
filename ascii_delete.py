class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        if len(s1) < len(s2):
            s1, s2 = s2, s1

        l1 = len(s1)
        l2 = len(s2)
        opt = [0]*(l2+1)
        for i in range(1, l2+1):
            opt[i] = opt[i-1] + ord(s2[i-1])
