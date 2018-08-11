class Solution:
    def numTilings(self, n):
        """
        :type N: int
        :rtype: int
        """
        ans = {1:1, 2:2, 3:5}
        if n in ans:
            return ans[n]
        magic = (10**9) + 7
        count = 0
        n = n*2
        trim_limit = (n//3)
        if n%3!=0:
            trim_limit+=1
        for i in range(0, trim_limit, 2):
            dom = (n-i*3)//2
            if dom >=0:
                count += 2*(dom-1) + i 
                count += 2*(dom//2)*(i//2)
                count = count%magic
        return count
s=Solution()
print(s.numTilings(4))