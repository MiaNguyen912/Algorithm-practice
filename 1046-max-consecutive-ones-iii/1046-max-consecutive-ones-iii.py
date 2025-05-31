class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # find max num of consecutive 1 if you can flip at most k 0's
        # flip: changing 0 to 1
        # -> find longest subarr with number of 0 <= k

        num_0 = 0
        l = 0
        max_len = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                num_0 += 1
            while num_0 > k: # invalid window -> cut left
                if nums[l] == 0:
                    num_0 -= 1
                l += 1
            # at this point, we have the longest valid window that end at 0
            max_len = max(max_len, r-l+1)
        return max_len
        