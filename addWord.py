

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.chars = {chr(i) for i in range(97, 123)}
        self.trie = {}
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        def _insert(w, wi, wl, cur_trie):
            if wi < wl:
                if w[wi] not in cur_trie:
                    cur_trie[w[wi]] = {}
                if wi == wl-1:
                    cur_trie[w[wi]]["leaf"] = True
                else:
                    _insert(w, wi+1, wl, cur_trie[w[wi]])

        _insert(list(word),0, len(word), self.trie)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def _search(w, wi, wl, cur):
            if wi > wl:
                return False
            elif wi == wl:
                if "leaf" in cur:
                    return True
            elif w[wi] == ".":
                for c in self.chars:
                    if c in cur:
                        ans = _search(w, wi+1, wl, cur[c])
                        if ans: return True
                return False
            elif wi < wl:
                if w[wi] in cur:
                    return _search(w, wi+1, wl, cur[w[wi]])
                return False

            return False
        return _search(list(word), 0, len(word), self.trie)
        



t = WordDictionary()
t.addWord("bat")
t.addWord("cat")
t.addWord("mat")
t.addWord("bet")
print(t.search("..."))