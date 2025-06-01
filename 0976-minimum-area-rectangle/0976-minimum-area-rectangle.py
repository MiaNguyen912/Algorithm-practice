class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort() # sort by x, then y
        print(points)
        min_area = math.inf
        for i in range(len(points)-3):
            x1,y1 = points[i]
            for j in range(i+3,len(points)):
                x2,y2 = points[j]
                if x1==x2 or y1==y2: # in not on a diagonal -> cant form a rect -> skip
                    continue
                area = abs(x2-x1) * abs(y2-y1)
                if area >= min_area: # if cannot be min anyway -> skip
                    continue
                else: # might be a min rect if 4 corners are in points -> need to validate this
                    # print("valid", (x1,y1), (x2,y2))
                    if ([x1,y2] in points and [x2,y1] in points):
                        min_area = min(min_area, area)
        return min_area if min_area is not math.inf else 0
