from collections import Counter, defaultdict
class Solution:
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        max_chars = defaultdict(int)
        for word in B:
        	word_counter = Counter(word)
        	for char in word_counter:
        		max_chars[char] = max(max_chars[char], word_counter[char])
        
        ans = []
        for word in A:
        	word_counter = Counter(word)
        	universal = True
        	for char in max_chars:
        		if max_chars[char] > word_counter[char]:
        			universal = False
        			break
        	if universal:
        		ans.append(word)
        return ans

A = ["amazon","apple","facebook","google","leetcode"]
B = ["e","o"]

A = ["amazon","apple","facebook","google","leetcode"]
B = ["l","e"]

A = ["amazon","apple","facebook","google","leetcode"]
B = ["e","oo"]

A = ["amazon","apple","facebook","google","leetcode"]
B = ["lo","eo"]

A = ["amazon","apple","facebook","google","leetcode"]
B = ["ec","oc","ceo"]

A = ["amazonum", "amazon","apple","facebook","google","leetcode"]
B = ["amazon"]
print(Solution().wordSubsets(A, B))


