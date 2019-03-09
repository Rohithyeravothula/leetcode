class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ord0 = ord('0')
        mapper = {'-':'sign', '+':'sign', 'e': 'exp'}
        for i in range(10):
            mapper[i] = 'num'
        def check(c):
            return mapper[c] if c in mapper else None

        def read_digits(s, i, l):
            while i<l and check(s[i]) == 'num':
                i+=1
            return i

        def check_sign(s, i, l):
            return i+1 if i<l and check(s[i]) == 'sign' else i

        def check_exp(s, i, l):
            if i==l: return False #can't end with e
            i = check_sign(s, i, l)
            if i==l:return False # can't end with sign
            i = read_digits(s, i, l)
            if i==l: return True
            return False

        s = s.strip()
        if s=='e' or s=='.' or s[:2]=='.e' or s=='-.':
            return False
        if not s:return False
        l,i = len(s),0
        i = check_sign(s, i, l)
        if i==l: return False
        i = read_digits(s, i, l)
                
        # integer
        if i==l: return True

        # integer with exp
        if check(s[i]) == 'exp':
            if i==0 or s[:2] == '+e' or s[:2] == '-e': return False # can't start with e
            return check_exp(s, i+1, l)

        # float
        if check(s[i]) == 'decimal':
            if i+1 == l: return True
            if (i+2) == l and check(s[i+1]) == "exp": return False
            i = read_digits(s, i+1, l)
            if i==l: return True
            # float with exp
            if check(s[i]) == 'exp':
                return check_exp(s, i+1, l)
            if i==l: return True
            return False
        return False

s = Solution()
# print(s.isNumber(".e1"))
while True:
    inp = input()
    print(s.isNumber(inp))
        



        