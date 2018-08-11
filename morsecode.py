class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = set()
        def morse_code(word):
            s=""
            for char in word:
                s+=code[ord(char) - ord('a')]
            return s
        for word in words:
            seen.add(morse_code(word))
        return len(seen)


wrds = []
s=Solution()
print(s.uniqueMorseRepresentations(wrds))
