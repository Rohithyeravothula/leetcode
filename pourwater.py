from heapq import heappush, heappop
class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        l = len(heights)
        K_index = K
        K_capicity = heights[K_index]
        left_min_heap = [(float("inf"), -1)]
        right_min_heap = [(float("inf"), -1)]
        for left_i in range(K-1, -1, -1):
            if heights[left_i] > K_capicity:
                break
            heappush(left_min_heap, (heights[left_i], left_i))

        for right_i in range(K+1, l):
            if heights[right_i] > K_capicity:
                break
            heappush(right_min_heap, (heights[right_i], right_i))

        center = heights[K]
        water = 0
        left_index = K_index-1
        right_index = K_index+1
        while water < V:
            min_left = heappop(left_min_heap)
            min_right = heappop(right_min_heap)
            if min_left[0] <= min_right[0] and min_left[0] < K_capicity:
                update = (min_left[0]+1, min_left[1])
                heappush(left_min_heap, update)
                heappush(right_min_heap, min_right)
                left_index+=1
            elif min_right[0] < min_left[0] and min_right[0] < K_capicity:
                update = (min_right[0]+1, min_right[1])
                heappush(left_min_heap, min_left)
                heappush(right_min_heap, update)
                right_index+=1
            else:
                K_capicity+=1
                heappush(left_min_heap, min_left)
                heappush(right_min_heap, min_right)
                for cur_left_i in range(left_i, -1, -1):
                    if heights[cur_left_i] > K_capicity:
                        break
                    heappush(left_min_heap, (heights[cur_left_i], cur_left_i))

                left_i = cur_left_i

                for cur_right_i in range(right_i, l):
                    if heights[cur_right_i] > K_capicity:
                        break
                    heappush(right_min_heap, (heights[cur_right_i], cur_right_i))

                right_i = cur_right_i

            water += 1

        ans = left_min_heap + right_min_heap
        result = [0]*l
        visited = set()
        for i in ans:
            if i[1] != -1:
                result[i[1]] = i[0]
                visited.add(i[1])
        for i in range(0, l):
            if i not in visited:
                visited.add(i)
                result[i] = heights[i]
        result[K_index] = K_capicity
        return result


hgts = [1,2,3,4]
vv=2
kk=2
s=Solution()
print(s.pourWater(hgts, vv,kk))

