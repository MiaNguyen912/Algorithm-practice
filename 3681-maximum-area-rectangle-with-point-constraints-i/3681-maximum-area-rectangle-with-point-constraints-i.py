class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        # points[i] = [xi, yi]
        # find max area of rectangle that can be formed with 4 points as its corners
        #           doesn't contain other point inside or on border
        #           parallel to axes
        # Return maximum area or -1

        # sort points by x
        # for points of same x, check if there's any point (called a) with a's y in the middle of their min and max y
        #   if a has same x as those point



        # bruteforce: for each point, for another point, check if these 2 points can form a rectangle, if yes, check if another points in inside this square


        if len(points) < 4:
            return -1
        points = sorted(map(tuple, points)) # [(1, 1), (1, 2), (1, 3), (3, 1), (3, 2), (3, 3)]

        print(points)
        points_set = set(points)
        max_area = -1
        for i in range(len(points) - 3):
            for j in range(i + 3, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2:  # if not diagonal
                    continue
                area = (x2 - x1) * (y2 - y1)  
                if area <= max_area: # if area isn't max, no need to check points
                    continue
                corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
                if (((x1, y2) in points_set) and 
                    ((x2, y1) in points_set) and
                    not any(x1 <= x <= x2 and y1 <= y <= y2 and (x, y) not in corners for x, y in points[i + 1: j])
                ):
                    max_area = max(area, max_area)
        return max_area