class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum
        # generate a prefix sum array of nums with pre[i] = sum of items in nums upto index i
        # for each pre[i], we'd want to find how many indices x s.t pre[x] = pre[i] - k and x <= i
        # => use a map to record number of occurence of items in pre upto the current i
        count = 0
        pre = 0
        mp = dict() # stores <sum([:i]): count>
        mp[0] = 1 # <sum([]) : 1>
        for i,curr in enumerate(nums):
            pre += curr
            target = pre - k
            count += mp.get(target, 0)
            mp[pre] =  mp.get(pre, 0) + 1
        return count

