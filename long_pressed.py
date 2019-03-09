class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if not name and not typed:
        	return True
        if not name or not typed:
        	return False
        nl = len(name)
        tl = len(typed)
        i = 0
        j = 0
        while i<nl and j<tl:
        	if name[i] == typed[j]:
        		i+=1
        		j+=1
        	else:
        		j+=1
        if i==nl and j==tl:
        	return True
        elif i==nl:
        	while j<tl:
        		if typed[j] != name[-1]:
        			return False
        		j+=1
        	return True
        return False

n,t="",""
n,t="","b"
n,t="leelee","lleeelee"
n,t="abc", "abccd"
print(Solution().isLongPressedName(n,t))