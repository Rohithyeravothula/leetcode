codes = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
# codes = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}

def get_val(r):
    return codes[r[0]]*16+codes[r[1]]

def get_dist(a,b):
    dist = get_val(a) - get_val(b+b)
    return dist*dist

class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        
        min_dist = float("inf")
        min_val = None
        color = color[1:]
        output = None
        for a in codes.keys():
            for b in codes.keys():
                for c in codes.keys():
                    dist = get_dist(color[0:2], a) + get_dist(color[2:4], b) + get_dist(color[4:], c)
                    if dist < min_dist:
                        min_dist = dist
                        min_val = a+b+c
                        output = "#{}{}{}{}{}{}".format(a,a,b,b,c,c)
                        # print(a+b+b, dist)
        return output


s=Solution()
print(s.similarRGB("#09f166"))
# print(get_dist("66", "6"))
