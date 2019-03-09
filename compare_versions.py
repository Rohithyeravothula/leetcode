class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        def strip(cur):
            l = len(cur)
            i,j = 0,l-1
            while i<l and cur[i] == " ":
                i+=1
            while j>=0 and cur[j] == " ":
                j-=1
            return cur[i:j+1]

        def split(cur):
            ans = []
            cur = strip(cur)
            l = len(cur)
            i = 0
            while i<l:
                prev = i
                while i<l and cur[i] != ".":
                    i+=1
                ans.append(int(cur[prev:i]))
                i+=1
            return strip_zeros(ans)

        def strip_zeros(a):
            l = len(a)
            j = l-1
            while j>=0 and a[j] == 0:
                j-=1
            return a[:j+1]
        if not version1 and not version2:
            return 0

        # v1 = strip_zeros([int(val) for val in version1.split(".")])
        # v2 = strip_zeros([int(val) for val in version2.split(".")])
        v1 = split(version1)
        v2 = split(version2)

        l1 = len(v1)
        l2 = len(v2)
        i,j = 0,0
        while i<l1 and j<l2:
            if v1[i] < v2[j]:
                return -1
            elif v1[i] > v2[j]:
                return 1
            else:
                i+=1
                j+=1
        if l1 == l2: return 0
        return 1 if i<l1 else -1

a,b = "",""
print(Solution().compareVersion(a,b))