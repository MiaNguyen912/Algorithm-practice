class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # return the min length of a subarray whose sum >= target, or 0 
        # time constraint: O(n) or O(n log(n))

        # sliding window
        # for each window ending at r, find a l closest to r such that sum of window >= target
        window_sum = 0
        l = 0
        min_len = math.inf
        for r,curr in enumerate(nums):
            window_sum += curr
            if window_sum >= target:
                while window_sum >= target:#cut left until getting shortest subarr with sum >= target
                    window_sum -= nums[l]
                    l += 1
                # at this point, window is the longest one ending at r that has sum < target
                # => adding one more item would make it becomes the shortest one with sum >= target
                min_len = min(min_len, r-l+1+1)
        return min_len if min_len != math.inf else 0


