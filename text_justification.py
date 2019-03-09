class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def get_repr(line):
            n = len(line)
            chars = sum([len(w) for w in line])
            if n == 1:
                spaces = maxWidth - chars
                return line[0] + " "*spaces
            dummy = []
            spaces = maxWidth - chars
            sp = spaces//(n-1)
            spr = spaces%(n-1)
            for word in line:
                dummy.append(word)
                ad = 1 if spr > 0 else 0
                if spr > 0: spr -= 1
                dummy.append(" "*(sp + ad))
            return "".join(dummy[:-1])

        def get_last_line(line):
            last_line = " ".join(line)
            spaces = maxWidth - len(last_line)
            return last_line + " "*spaces

        result = []
        l = len(words)
        i = 0
        while i<l:
            cur = maxWidth
            dummy = []
            while i<l and cur > 0:
                wl = len(words[i])
                if wl <= cur:
                    cur = cur-wl-1
                    dummy.append(words[i])
                    i+=1
                else:
                    break
            if i!=l:
                result.append(get_repr(dummy))
            else:
                result.append(get_last_line(dummy))
        return result


inp = ["Science","is","what","we","understand","well","enough","to","explain", "to","a","computer.","Art","is","everything","else","we","do"]
wid = 20
inp = ["ab", "cd"]
wid = 5
inp = ["What","must","be","acknowledgment","shall","be"]
inp = ["This", "is", "an", "example", "of", "text", "justification."]
wid = 16

print(Solution().fullJustify(inp, wid))


