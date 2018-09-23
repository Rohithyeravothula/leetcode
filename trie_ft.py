class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def insert(self, word):
        """
        Inserts a word into the trie.
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
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        def _search(w, wi, wl, cur):
            if wi == wl and "leaf" in cur:
                return True
            elif wi < wl:
                if w[wi] in cur:
                    return _search(w, wi+1, wl, cur[w[wi]])
                return False
            return False
        return _search(list(word), 0, len(word), self.trie)

    def startsWith(self, word):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        def _startsWith(w, wi, wl, cur):
            if wi == wl:
                return True
            if w[wi] in cur:
                return _startsWith(w, wi+1, wl, cur[w[wi]])
            return False
        return _startsWith(list(word), 0, len(word), self.trie)
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("hello")
obj.insert("hell")
obj.insert("help")
obj.insert("apple")
# print(obj.trie)
print(obj.startsWith("help"))
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)