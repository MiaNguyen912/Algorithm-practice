class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # keep a max heap of distance of points to 0
        # for each point: if heap still has space -> add point, 
        #                   else compare the distance of it to 0 and the max item in heap
        # => O(n) time, O(k) space
        max_h = []
        for p in points:
            distance = math.sqrt(p[0]**2 + p[1]**2)
            if len(max_h) < k:
                heappush(max_h, [-distance, p[0], p[1]])
            else:
                max_distance_in_h = -max_h[0][0]
                if distance < max_distance_in_h:
                    heappop(max_h)
                    heappush(max_h, [-distance, p[0], p[1]])
        return [[x,y] for [d,x,y] in max_h]

        # M2: using heap and lambda
        return heapq.nsmallest(k, points, key=lambda p: p[0] ** 2 + p[1] ** 2)
