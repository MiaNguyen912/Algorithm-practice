class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # start from building 0 and move to the next building by using bricks or ladders.   
        # If current building's height >= next building, dont need a ladder or bricks.
        # else,  either use 1 ladder or (h[i+1] - h[i]) bricks.
        # Return the furthest building you can reach 
        # at least 1 building in heights
        # bricks, ladders can be 0

        # plan: use up n ladders for n first gaps and record these n gaps in a min heap
        # for the next gap, compare it with the min gap in heap, 
        #       if this_gap > min_gap: it means we could replace the ladder used at min_gap with this_gap
        # move to next gap until we use up bricks:

        # min_h = []
        # curr_building = 0
        # while curr_building<len(heights)-1: # while not the last building
        #     gap = heights[curr_building]-heights[curr_building+1]
        #     if gap >= 0: # no need ladder/brick
        #         curr_building += 1
        #     else: # use ladder
        #         if ladders > 0:  # 0 <= ladders <= heights.length
        #             heappush(min_h, (abs(gap)))
        #             ladders -= 1
        #             curr_building +=1
        #         else: # couldn't go without ladder but we have no ladder left -> break
        #             break
        # while curr_building<len(heights)-1:
        #     gap = heights[curr_building]-heights[curr_building+1]
        #     if gap >= 0: # no need ladder/brick
        #         curr_building += 1
        #         continue
        #     if bricks <= 0:
        #         break
        #     min_gap_from_heap = math.inf
        #     if min_h:
        #         min_gap_from_heap = heappop(min_h)
        #     if abs(gap) > min_gap_from_heap: # use ladder for this gap instead of the min_gap_from_heap, use brick for min_gap_from_heap
        #         bricks -= min_gap_from_heap
        #     else:
        #         bricks -= abs(gap) # use bricks for current gap
        #     # print("--", min_gap_from_heap, gap, bricks)
        #     if bricks > 0:
        #         curr_building += 1
        # return curr_building

        gap_min_h = []
        for i in range(len(heights)-1):
            if heights[i+1] <= heights[i]: # no need ladder/bricks
                continue
            gap = heights[i+1] - heights[i]
            heappush(gap_min_h, gap)
            if ladders >0: # use up ladders
                ladders -= 1
            else: # start using bricks
                min_gap = heappop(gap_min_h)
                bricks -= min_gap
                if bricks < 0:
                    return i
        return len(heights) - 1




            

