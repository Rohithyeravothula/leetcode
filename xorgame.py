class Solution:
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_length = len(nums)
        if nums_length == 0:
            return True
        def result(cur_xor, elements, l):
            # print(cur_xor, elements)
            if not cur_xor or l==0:
                store[(cur_xor, "".join(map(str, elements)))] = True
                return True
            if (cur_xor, "".join(map(str, elements))) in store:
                return store[(cur_xor, "".join(map(str, elements)))]
            for i in range(0, l):
                elements[i], elements[0] = elements[0], elements[i]
                if not result(cur_xor ^ elements[0], elements[1:], l-1):
                    store[(cur_xor, "".join(map(str, elements)))] = True
                    return True
                elements[i], elements[0] = elements[0], elements[i]
            store[(cur_xor, "".join(map(str, elements)))] = False
            return False
        nums_xor = nums[0]
        for n in nums[1:]:
            nums_xor = nums_xor ^ n
        store = {}
        nums = list(set(nums))
        ans = result(nums_xor, nums, len(nums))
        if (nums_length - len(nums))%2==0:
            return ans
        return not ans
            


inp = [1,0,0,0,1,0,0,0,1,0,1]
s=Solution()
print(s.xorGame(inp))