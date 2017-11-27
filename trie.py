class Trie(object):

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
        def insert_word(w, d):
            if len(w) == 1:
                if w in d:
                    d[w]["leaf"] = 1
                else:
                    d[w] = {"leaf":1}
            else:
                t = w[0]
                if t not in d:
                    d[t] = {}
                insert_word(w[1:], d[t])
        if len(word) != 0:
            insert_word(word, self.trie)
        print(self.trie)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        def search_word(w, d):
            if len(w) == 1:
                if w in d and "leaf" in d[w]:
                    return True
                return False
            else:
                if w[0] in d:
                    return search_word(w[1:], d[w[0]])
                return False
        if len(word) != 0:
            return search_word(word, self.trie)
        return False

        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        def starts(w, d):
            # print(w, d)
            if len(w) == 1:
                if w in d and "leaf" not in d[w]:
                    return True
                return False
            else:
                if w[0] in d:
                    return starts(w[1:], d[w[0]])
                return False

        if len(prefix) == 0:
            return True
        return starts(prefix, self.trie)

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("abc")
print(obj.search("abc"))
print(obj.search("ab"))
obj.insert("ab")
print(obj.search("ab"))
print(obj.trie["a"]["b"])

# obj.insert("ab")
# print(obj.search("ab"))
# obj.insert("ab")
# print(obj.search("ab"))