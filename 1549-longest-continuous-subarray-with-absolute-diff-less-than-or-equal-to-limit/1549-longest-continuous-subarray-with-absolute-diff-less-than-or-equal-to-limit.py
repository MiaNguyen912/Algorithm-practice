class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # size of longest subarr with |diff between any 2 items| <= limit
        # => max size that |diff between largest and smallest items| <= limit
        # sliding window
        # for each r, find the leftmost l that satisfy


        # prefix min/max
        # n = len(nums)
        # premin = [0]*(n+1)
        # for i in range(n+1):
        #     premin[i] = min(premin[i-1], nums[i-1])
        # premax = [0]*(n+1)
        #     premax[i] = max(premax[i-1], nums[i-1])
        
        # for r in range(n+1):



        size = 0
        l=0
        sorted_l = SortedList([])
        for r in range(len(nums)):
            sorted_l.add(nums[r])
            while abs(sorted_l[0]-sorted_l[-1]) > limit and l <r: # cut left
                sorted_l.discard(nums[l])
                l += 1
            size = max(size, r-l+1)
        return size






    
        