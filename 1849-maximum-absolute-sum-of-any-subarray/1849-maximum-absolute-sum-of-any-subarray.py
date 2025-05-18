class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # prefix sum
        lmax = lmin = 0
        prefix_sum = 0
        result = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            result = max(result, abs(prefix_sum - lmin), abs(prefix_sum - lmax))
            lmax = max(lmax, prefix_sum)
            lmin = min(lmin, prefix_sum)
            # print('pre: ', prefix_sum, ' -- result: ', result, '-- lmax: ' , lmax, ' -- lmin: ', lmin)
        return result