class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # In one operation, either remove the leftmost or rightmost element from nums and subtract its value from x. 
        # Return the min number of operations to reduce x to 0 if it is possible, otherwise, return -1.


        # M1: prefix sum
        # let l, r be the range of subarr after removed element to reduce x to 0
        # -> sum(nums[l->r]) = sum(nums) - x
        # => find longest subarr l->r such that sum(nums[l->r]) = sum(nums) - x = target
        # => use prefix sum (pre[r] - pre[l-1] = target)

        # pre_r = 0
        # target = sum(nums) - x
        # if target == 0: # if x is sum of all items, we need to remove len(nums) items
        #     return len(nums)
        # mp = defaultdict(lambda: math.inf)  # map stores pairs <sum[subarr[0->i]] : i> (i is the leftmost possible index)
        # mp[0] = -1 # store pair <sum([]) : -1>
        # max_len = 0 
        # for r in range(len(nums)):
        #     pre_r += nums[r]
        #     pre_l = pre_r - target
        #     if pre_l in mp:
        #         max_len = max(max_len, r - mp[pre_l])
        #     mp[pre_r] = min(mp[pre_r], r)
        # if max_len == 0:
        #     return -1
        # return len(nums) - max_len


        #--------------------------
        # M2: sliding window (faster)
        target = sum(nums) - x
        if target == 0:
            return len(nums)
        l = max_len = 0
        window_sum = 0
        for r in range(len(nums)):
            window_sum += nums[r]
            while window_sum > target and l<=r: # cut left
                window_sum -= nums[l]
                l += 1
            if window_sum == target:
                max_len = max(r - l + 1, max_len)
        return len(nums) - max_len if max_len != 0 else -1