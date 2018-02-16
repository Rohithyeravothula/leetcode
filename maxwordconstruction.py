
class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words = set(words)
        output = ""
        output_length = 0
        for word in words:
        	valid = True
        	l = len(word)
        	for i in range(0,l):
        		if word[:i+1] not in words:
        			valid = False
        	if valid and len(word) == output_length and word < output:
        		output = word
        	if valid and len(word) > output_length:
        		output_length = len(word)
        		output = word
        return output


dd = ["ew", "ewq", "ewqz"]
s=Solution()
print(s.longestWord(dd))

