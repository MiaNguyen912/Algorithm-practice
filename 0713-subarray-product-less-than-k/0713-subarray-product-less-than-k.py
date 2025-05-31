class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # count num of subarr where product < k
        # => find longest subarr from l -> r s.t product < k


        window_product = 1
        l = 0
        count = 0
        
        for r in range(len(nums)):
            window_product *= nums[r]
            while window_product >= k and l <= r: # cut left
                window_product /= nums[l]
                l += 1
            if window_product < k:
                # at this point, subarr from l->r is the longest one with product < k
                while nums[l-1] == 1 and l > 0: # handle multiplying by 1
                    l -= 1
                count += r-l+1
        return count

