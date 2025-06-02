class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # prefix sum
        # sum = |pre[r] - pre[l]|
        # for each pre[r], sum can be max only when pre[l] is either 
        #       - smallest (|1-(-10)| = 11)
        #       - or largest (|1-12| = 11)

        lmax = lmin = 0
        prefix_sum = 0
        result = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            result = max(result, abs(prefix_sum - lmin), abs(prefix_sum - lmax))
            lmax = max(lmax, prefix_sum)
            lmin = min(lmin, prefix_sum)
        return result

