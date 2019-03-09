class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for ch in s:
            if ch in {'a', 'b'}:
                stk.append(ch)
            else:
                v1 = stk.pop() if stk else None
                v2 = stk.pop() if stk else None
                if v1 != 'b' or v2 != 'a':
                    return False
        return stk == []

# inp = "cababc"
while True:
    print(Solution().isValid(input()))
