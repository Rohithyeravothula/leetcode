class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        list1dict = {}
        l1 = len(list1)
        l2 = len(list2)
        for i in range(0, l1):
            if list1[i] not in list1dict:
                list1dict[list1[i]] = i
        ans = float("inf")
        min_ans = []
        for i in range(0, l2):
            if list2[i] in list1dict:
                if ans == i+list1dict[list2[i]]:
                    min_ans.append(list2[i])
                elif ans > i+list1dict[list2[i]]:
                    ans = min(ans, i+list1dict[list2[i]])
                    min_ans = [list2[i]]
        return min_ans

left = ["Shogun","Tapioca Express","Burger King","KFC"]
right = ["KFC","Shogun","Burger King"]
s=Solution()
print(s.findRestaurant(left, right))