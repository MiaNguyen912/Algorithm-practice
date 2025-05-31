class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # In one operation, either remove the leftmost or rightmost element from nums and subtract its value from x. 
        # Return the min number of operations to reduce x to 0 if it is possible, otherwise, return -1.
        # all 

        # let l, r be the range of subarr after removed element to reduce x to 0
        # -> sum(nums[l->r]) = sum(nums) - x
        # => find longest subarr l->r such that sum(nums[l->r]) = sum(nums) - x = target
        # => prefix sum (pre[r] - pre[l-1] = target)

        pre = [nums[0]] * len(nums)
        for i in range(1,len(nums)):
            pre[i] = pre[i-1] + nums[i]
        target = pre[-1] - x
        if target == 0: # if x is sum of all items, we need to remove len(nums) items
            return len(nums)
        mp = defaultdict(lambda: math.inf)  # map stores pairs <sum[subarr[0->i]] : i> (i is the leftmost possible index)
        mp[0] = -1 # store pair <sum([]) : -1>
        max_len = -1 

        # print("target: ", target)
        for r in range(len(nums)):
            pre_l = pre[r] - target
            if pre_l in mp:
                max_len = max(max_len, r - mp[pre_l])
                # print("max_len: ", max_len)
            mp[pre[r]] = min(mp[pre[r]], r)
        if max_len == -1:
            return -1
        return len(nums) - max_len