class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        hPeople = {}
        for i in people:
            if i[0] in hPeople:
                hPeople[i[0]].append(i[1])
            else:
                hPeople[i[0]] = [i[1]]

        heights = list(hPeople.keys())
        # print(heights)
        heights.sort(reverse=True)

        ans = []
        for h in heights:
            ks = hPeople[h]
            ks.sort()
            for k in ks:
                ans.insert( k ,(h, k))
                # print(ans, (h, k))
        return ans


a=[[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]
s=Solution()
print(s.reconstructQueue(a))

