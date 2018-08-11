class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""
        ans = ""
        vovels = {'a', 'e', 'i', 'o', 'u'}
        endstr = "a"
        for word in S.split(" "):
        	if word[0].lower() in vovels:
        		ans += word + "ma" + endstr + " "
        	else:
        		ans += word[1:] + word[0] + "ma" + endstr + " "
        	endstr = endstr + "a"
        return ans[:-1]


s = Solution()
print(s.toGoatLatin("")) 