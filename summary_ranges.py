class Solution:
    def summaryRanges(self, a):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        l = len(a)
        i=0
        while i<l:
            j = i
            x,y = i,l-1
            s=i
            while x<=y:
                m = (x+y)>>1
                val,idx = a[m]-a[i], m-i
                # print(val, idx)
                if val == idx:
                    s=m
                    x=m+1
                elif val > idx:
                    y=m-1
                else:
                    x=m+1
            # print(s)
            if s>i:
                ranges.append("{}->{}".format(a[i], a[s]))
            else:
                ranges.append("{}".format(a[i]))
            i=s+1
        return ranges


inp = []
print(Solution().summaryRanges(inp))

        