class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # size of longest subarr with |diff between any 2 items| <= limit
        # => max size that |diff between largest and smallest items| <= limit
        # sliding window
        # for each r, find the leftmost l that satisfy

        # time O(nlogn), space O(n)
        size = 0
        l=0
        sorted_l = SortedList([])
        for r in range(len(nums)):
            sorted_l.add(nums[r])
            while sorted_l[-1]-sorted_l[0] > limit: # cut left
                sorted_l.discard(nums[l])
                l += 1
            size = max(size, r-l+1)
        return size






    
        