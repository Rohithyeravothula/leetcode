class Solution:
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        def get_groups(input_string):
            if not input_string:
                return []

            groups = []
            cur = None
            i = 0
            count = 0
            l = len(input_string)
            while i<l:
                cur = input_string[i]
                count = 1
                i+=1
                while i<l and input_string[i] == cur:
                    count += 1
                    i+=1
                groups.append((cur, count))

            return groups

        # return get_groups(S)

        s_groups = get_groups(S)
        l = len(s_groups)
        number_words = 0
        for word in words:
            extendable = True
            word_groups = get_groups(word)
            if len(word_groups) == l:
                for i in range(0, l):
                    if word_groups[i][0] == s_groups[i][0]:
                        if word_groups[i][1] != s_groups[i][1]:
                            if word_groups[i][1] >= 3 and word_groups[i][1] > s_groups[i][1]:
                                extendable = False
                                break
                            elif word_groups[i][1] < 3 and s_groups[i][1] < 3:
                                extendable = False
                                break
                    else:
                        extendable = False

            else:
                extendable = False
            if extendable:
                number_words += 1
        return number_words





inp = "a"
wds = ["", ""]
s=Solution()
print(s.expressiveWords(inp, wds))


