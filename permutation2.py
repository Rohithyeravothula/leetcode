class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def build(a, j, l):
            if j==l-1:
                return [[a[j]]]
            result = []
            i = j
            seen = set()
            while i<l:
                a[j], a[i] = a[i], a[j] # swaping 
                local = build(a, j+1, l)
                for seq in local:
                    result.append([a[j]] + seq)
                a[j], a[i] = a[i], a[j]
                seen.add(a[i])
                i+=1
                while i<l and a[i] in seen:
                    i+=1
            return result
        l = len(nums)
        return build(nums, 0, l)


from pprint import pprint
inp = [3]
inp = []
inp = [0,1,0,0,9]
ans = Solution().permuteUnique(inp)
ans = ["".join([str(i) for i in val]) for val in ans]
print(ans)
print(list(set(ans)))
