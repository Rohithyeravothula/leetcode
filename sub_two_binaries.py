class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s = ""
        a,b = a[::-1], b[::-1]
        la,lb = len(a), len(b)
        l = max(la, lb)
        i = 0
        carry = 0
        while i<l or carry==1:
        	b1 = int(a[i] if i<la else 0)
        	b2 = int(b[i] if i<lb else 0)
        	curbit = b1^b2^carry
        	carry = (b1&b2)|(carry&(b1|b2))
        	s += str(curbit)
        	# print(curbit, carry)
        	i+=1

        return s[::-1]

a,b="000", "000000"
print(Solution().addBinary(a,b))
