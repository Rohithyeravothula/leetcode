class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l = len(s)
        d={}
        v = 0
        start = 0
        end = 0
        while end < l