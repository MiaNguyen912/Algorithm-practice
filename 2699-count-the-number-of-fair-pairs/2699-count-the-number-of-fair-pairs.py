class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # find num fair pairs
        # count number of items from a->b: bisect_right() - bisect_left()
        # lower <= nums[i] + nums[j] <= upper
        # => lower - nums[j] <= nums[i] <= upper - nums[j]
        # => for each j, num of i that satisfies condition = bisect_right(nums, upper - nums[j], 0, j) - bisect_left(nums, lower - nums[j], 0, j)

        nums.sort()
        res = 0
        for j in range(len(nums)):
            res += bisect_right(nums, upper - nums[j], 0, j) - bisect_left(nums, lower - nums[j], 0, j)
        return res