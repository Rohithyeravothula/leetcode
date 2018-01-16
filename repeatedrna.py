class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        code_map = {'A': "00", 'C':"01", 'G': "10", 'T':"11"}
        def hashcode(a):
            bcode = ""
            for i in a:
                bcode += code_map[i]
            return int(bcode, 2)

        def roll(a, c):
            return ((a & 1<8) << 2) & int(code_map[c], 2)

        l = len(s)
        prev = hashcode(s[0:10])
        print(prev)
        counter = {prev:1}
        ans = set()
        for i in range(1, l-9):
            cur_hash = roll(prev, s[i])
            print(prev, cur_hash)
            if cur_hash in counter:
                ans.add(s[i:i+10])
            else:
                counter[cur_hash] = 1
            prev = cur_hash
        print(list(ans))
        return list(ans)

s=Solution()
s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")