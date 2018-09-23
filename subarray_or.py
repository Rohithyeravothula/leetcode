class Solution:
    def subarrayBitwiseORs(self, a):
        """
        :type A: List[int]
        :rtype: int
        """
        seen = set([a[0]])
        prev_seen = set([a[0]])
        for val in a[1:]:
        	cur_seen = set([val])
        	seen.add(val)
        	for ps in prev_seen:
        		cur_seen.add(ps | val)
        		seen.add(ps | val)
        	prev_seen = cur_seen
        return len(seen)

print(Solution().subarrayBitwiseORs([]))