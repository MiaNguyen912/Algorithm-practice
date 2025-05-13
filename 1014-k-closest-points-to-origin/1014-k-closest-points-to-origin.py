class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # keep a max heap of distance of points to 0
        # for each point: if heap still has space -> add point, 
        #                   else compare the distance of it to 0 and the max item in heap
        # => O(n) time, O(k) space
        max_h = []
        for x,y in points:
            dist = x**2 + y**2 # we can skip the sqrt()
            if len(max_h) < k:
                heappush(max_h, [-dist, x, y])
            else:
                max_dist_in_h = -max_h[0][0]
                if dist < max_dist_in_h:
                    heappushpop(max_h, [-dist, x,y])
        return [[x,y] for [d,x,y] in max_h]

        # M2: using heap and lambda
        return heapq.nsmallest(k, points, key=lambda p: p[0] ** 2 + p[1] ** 2)
