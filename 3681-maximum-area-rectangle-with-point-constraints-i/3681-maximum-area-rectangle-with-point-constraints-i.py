class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        # points[i] = [xi, yi]
        # find max area of rectangle that can be formed with 4 points as its corners
        #           doesn't contain other point inside or on border
        #           parallel to axes
        # Return maximum area or -1

        # M1: bruteforce (O(n^3))
        # sort points by x
        # for each 2 points, check if these 2 points can form a rectangle (are on a diagonal)
        # if yes, check if there's any other points in inside this rect
        if len(points) < 4:
            return -1
        points = sorted(points) # [[1, 1], [1, 3], [3, 1], [3, 3]]
        points_set = set([tuple(p) for p in points]) # change to set since `if i in points_set` is O(1)
        # print(points_set) # {(3, 1), (1, 1), (3, 3), (1, 3)}

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
                corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)] #corners of the rect containing (x1, y1),(x2, y2) 
                if (((x1, y2) in points_set) and ((x2, y1) in points_set) and
                    not any(x1 <= x <= x2 and y1 <= y <= y2 and (x, y) not in corners for x, y in points[i + 1: j])
                ):
                    max_area = max(area, max_area)
        return max_area

