class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        start = 0
        end = 0
        curL = 0
        maxL = 0
        visited = {}
        while start < size and end < size:
            print(start, end, visited, curL)
            if s[end] in visited:
                del visited[s[start]]
                start += 1
                curL = end - start
            else:
                visited[s[end]] = 1
                curL = end - start + 1
                end += 1
            if maxL < curL:
                maxL = curL
        return maxL


s = Solution()
print(s.lengthOfLongestSubstring(""))


"""
dp
start at every point and construct the longest substring
repeated calculation of substrings => overlapping subproblems
solving subproblems can solve the solution => every char, either forms a bigger substring or not 

d[i, j] = max substring at that can be formed from i starting to j
d[0, 0] = 0
d[i, j] = max(1+d[i, j-1], 1+d[i+1, j], )

a => ab

ab => abc

ba => bab
dvdf => d, dv, dvd=>vd, vdf
devfvrqt => d, de, dev, devf, devfv => evfv

d@c=> n/2, n/2, check on boundary

linear time=>
visited => map of char to position
cur len, check current char, if visited then change cur len else proceed

"""
