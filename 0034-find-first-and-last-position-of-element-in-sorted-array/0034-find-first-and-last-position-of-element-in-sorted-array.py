class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # nums: non-decreasing
        # find starting and ending position of target or [-1,-1]
        # O(log n) time
        
        # plan: find the first and last indices of target
        # binary search
        # find smallest index of item == target (use bisect_left())
        # and smallest index of item > target (use bisect_right())

        # bisect_left(array, x) => find smallest index of item >= x, or len(array) if x > all items, or 0 if x < all
        # bisect_right(arr, x) => find smallest index of item > x, or len(array) if x > all items, or 0 if x < all 

        l = bisect_left(nums, target)
        if l > len(nums)-1 or nums[l] != target:
            return [-1,-1]
        r = bisect_right(nums, target)
        return [l,r-1]