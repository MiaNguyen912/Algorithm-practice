class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # In one operation, either remove the leftmost or rightmost element from nums and subtract its value from x. 
        # Return the min number of operations to reduce x to 0 if it is possible, otherwise, return -1.
        # all 

        # let l, r be the range of subarr after removed element to reduce x to 0
        # -> sum(nums[l->r]) = sum(nums) - x
        # => find longest subarr l->r such that sum(nums[l->r]) = sum(nums) - x = target
        # => prefix sum (pre[r] - pre[l-1] = target)

        # pre = [nums[0]] * len(nums)
        # for i in range(1,len(nums)):
        #     pre[i] = pre[i-1] + nums[i]
        pre_r = 0
        target = sum(nums) - x
        if target == 0: # if x is sum of all items, we need to remove len(nums) items
            return len(nums)
        mp = defaultdict(lambda: math.inf)  # map stores pairs <sum[subarr[0->i]] : i> (i is the leftmost possible index)
        mp[0] = -1 # store pair <sum([]) : -1>
        max_len = -1 

        for r in range(len(nums)):
            pre_r += nums[r]
            pre_l = pre_r - target
            if pre_l in mp:
                max_len = max(max_len, r - mp[pre_l])
            mp[pre_r] = min(mp[pre_r], r)
        if max_len == -1:
            return -1
        return len(nums) - max_len



        # target = sum(nums) - x
        # n = len(nums)
        # if target < 0:
        #     return -1
        # if target == 0:
        #     return n
        # left = ans = 0
        # sum_ = 0
        # for right, x in enumerate(nums):
        #     sum_ += x
        #     while sum_ > target:
        #         sum_ -= nums[left]
        #         left += 1
        #     if sum_ == target:
        #         ans = max(right - left + 1, ans)
        # return n - ans if ans != 0 else -1