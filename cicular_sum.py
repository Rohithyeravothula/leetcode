class Solution:
    def maxSubarraySumCircular(self, a):
        """
        :type A: List[int]
        :rtype: int
        """
        l = len(a)
        if l==1:
        	return a[0]

        a = a+a
        l2 = len(a)
        opt = [0]*l2
        opt[0] = a[0]
        i = 1
        c = 1
        for i in range(1, l2):
            opt[i] = max(opt[i-1]+a[i], a[i])
            if opt[i] == a[i]:
                c = 1
            else:
                c+=1
            if c==l:
                break
        print(opt)
        return max(opt)


inp = [4]
inp = [-4]
inp = [-3, -2, -1]
inp = [5,-2,5]
print(Solution().maxSubarraySumCircular(inp))
        