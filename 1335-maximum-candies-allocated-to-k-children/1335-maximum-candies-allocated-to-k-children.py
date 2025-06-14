class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # similar to koko eating bananas
        # You should allocate piles of candies to k children such that each child gets the same number of candies. 
        # Each child can be allocated candies from only one pile of candies and some piles of candies may go unused.
        # find max num of candies each child gets or 0
        # k: num children

        # plan: for each number of candies from 0 to min(candies), find max one that satisfies condition
        # condition: sum(candies[i] / current_num_candies) >= 11

        def check(num_candies_per_child):
            num_children_has_candies = 0
            for c in candies:
                num_children_has_candies += (c//num_candies_per_child)
                if num_children_has_candies >= k:
                    return True
            return False

        l,r = 1,max(candies)
        while l<=r:
            mid = (l+r)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r