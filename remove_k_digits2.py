class Solution:
    def removeKdigits(self, num: 'str', k: 'int') -> 'str':
        stk = []
        num = list([int(v) for v in num])
        if k > len(num) or not num:
            return "0"
        for v in num:
            if not stk:
                stk.append(v)
            else:
                while k>0 and stk and stk[-1] > v:
                    stk.pop()
                    k-=1
                stk.append(v)

        # remove leading zeros
        stk = stk[::-1]
        while stk and stk[-1] == 0:
            stk.pop()
        stk = stk[::-1]
        if not stk or k == len(stk):
            return "0"

        res = "".join([str(v) for v in stk])
        return res if k==0 else res[:-k]

print(Solution().removeKdigits("10", 1))
