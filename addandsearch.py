class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        def _add(curlevel, curword):
            letter = curword[0]
            if letter not in curlevel:
                curlevel[letter] = {}
            if len(curword) == 1:
                curlevel[letter]["leaf"] = {}
            else:
                _add(curlevel[letter], curword[1:])

        if len(word) >= 1:
            _add(self.trie, word)

        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def _lookup(curlevel, word):
            if len(word) == 1:
                if word == ".":
                    for i in curlevel:
                        if "leaf" in curlevel[i]:
                            return True
                    return False
                else:
                    if word in curlevel and "leaf" in curlevel[word]:
                        return True
                    return False
            else:
                letter = word[0]
                if letter == ".":
                    for i in curlevel:
                        if _lookup(curlevel[i], word[1:]):
                            return True
                    return False
                else:
                    if letter in curlevel:
                        return _lookup(curlevel[letter], word[1:])
                    return False
        if len(word) >= 1:
            return _lookup(self.trie, word)
        return False



# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("")
obj.addWord("pbe")
print(obj.search(""))
# print(obj.trie)

# param_2 = obj.search(word)