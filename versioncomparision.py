class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        def convert(version):
            ans = []
            for v in version:
                ans.append(str(int(v)))
            l = len(ans)
            i = l-1
            while i>=0 and ans[i] == "0":
                i-=1
            return ans[0:i+1]

        v1 = convert(version1.split("."))
        v2 = convert(version2.split("."))
        if ".".join(v1) == ".".join(v2):
            return 0
        v1l = len(v1)
        v2l = len(v2)
        l = min(v1l, v2l)
        i = 0
        ans = 1 # left is bigger
        while i<l:
            if int(v1[i]) < int(v2[i]):
                ans = -1
                break
            elif int(v1[i]) == int(v2[i]):
                i+=1
            else:
                return 1

        if ans == -1:
            return -1
        else:
            if ".".join(v1[:i]) == ".".join(v2[:i]):                
                if len(v1) < len(v2):
                    return -1
            return 1

s=Solution()
print(s.compareVersion("0.1", "1.0"))