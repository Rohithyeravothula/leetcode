class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        def get_sign(a):
            if a==0:
                return 1
            return a/abs(a)
        s = 0
        c = 0
        i = 0
        sign = get_sign(a) * get_sign(b)
        while (1<<i <= a) or (1<<i <= b):
            b1, b2 = (a>>i)&1, (b>>i)&1
            bi = (b1^b2^c)
            s = (bi << i) | s
            c = (b1&c) | (b2&c) | (b1&b2)
            i+=1
        if sign:
            s = (c<<i) | s
            if get_sign(a) == -1 and get_sign(b) == -1:
                return -s
            return s
        else:
            

            
s = Solution()
print(s.getSum(0,42))