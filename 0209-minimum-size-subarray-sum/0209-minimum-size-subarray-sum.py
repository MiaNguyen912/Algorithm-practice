class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # return the min length of a subarray whose sum >= target, or 0 
        # time constraint: O(n) or O(n log(n))

        w_sum = 0
        l = 0
        min_len = math.inf 
        for r in range(len(nums)):
            w_sum += nums[r]
            if w_sum >= target: 
                while w_sum >= target: # cut left until we find a shortest subarr with sum >= target
                    w_sum -= nums[l]
                    l += 1
                min_len = min(min_len, r-l+1+1)
        return min_len if min_len is not math.inf else 0 
            
